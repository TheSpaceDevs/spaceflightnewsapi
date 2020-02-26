const chai = require('chai');
const expect = require('chai').expect;
const chaiHttp = require('chai-http');

const app = require('../app');

chai.use(chaiHttp);

describe('Articles', () => {
  it('List all articles, expect it to have a length of 10 and status code 200', (done) => {
    chai.request(app)
      .get('/api/v1/articles')
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res.body.docs).to.be.an('array');
        expect(res.body.docs).to.have.length(10);
        done()
      });
  });

  it('List all articles on the second page, expect it to have a length of 10 and status code 200', (done) => {
    chai.request(app)
      .get('/api/v1/articles?page=2')
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res.body.docs).to.be.an('array');
        expect(res.body.docs).to.have.length(10);
        done()
      });
  });

  it('Get a single article, expect it to be an array and status code 200', (done) => {
    chai.request(app)
      .get('/api/v1/articles?_id=5e1d86133f939d8c65a308ff')
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res.body.docs).to.be.an('array');
        expect(res.body.docs).to.have.length(1);
        done()
      });
  });

  it('Get all articles by SpaceX, expect it to be an array with a length of 10 and status code 200', (done) => {
    chai.request(app)
      .get('/api/v1/articles?news_site=spacex')
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res.body.docs).to.be.an('array');
        res.body.docs.forEach(article => {
          expect(article.news_site).to.eql('spacex')
        });
        done()
      });
  });

  it('List 5 articles, expect it to have a length of 5 and status code 200', (done) => {
    chai.request(app)
      .get('/api/v1/articles?limit=5')
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res.body.docs).to.be.an('array');
        expect(res.body.docs).to.have.length(5);
        done()
      });
  });

  it('Post a new article without auth, expecting a 403 and forbidden', (done) => {
    chai.request(app)
      .post('/api/v1/articles')
      .send({
        'news_site': 'test_site',
        'news_site_long': 'Test Site',
        'title': 'Test Article',
        'url': 'https://spaceflightnewsapi.net',
        'featured_image': 'https://snapi.space'
      })
      .end((err, res) => {
        expect(res).to.have.status(401);
        expect(res.unauthorized).eql(true);
        done()
      });
  });
});
