const chai = require('chai');
const expect = require('chai').expect;
const chaiHttp = require('chai-http');

const app = require('../app');

chai.use(chaiHttp);

describe('Blogs', () => {
  it('List all blogs, expect it to have a length of 10 and status code 200', (done) => {
    chai.request(app)
      .get('/api/v1/blogs')
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res.body.docs).to.be.an('array');
        expect(res.body.docs).to.have.length(10);
        done()
      });
  });

  it('List all blogs on the second page, expect it to have a length of 10 and status code 200', (done) => {
    chai.request(app)
      .get('/api/v1/blogs?page=2')
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res.body.docs).to.be.an('array');
        expect(res.body.docs).to.have.length(10);
        done()
      });
  });

  it('Get a single blog, expect it to be an array with a length of 10 and status code 200', (done) => {
    chai.request(app)
      .get('/api/v1/blogs?_id=5c8188932568aa81ffc44fe1')
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res.body.docs).to.be.an('array');
        expect(res.body.docs).to.have.length(1);
        done()
      });
  });

  it('Get all blogs by planetarysociety, expect it to be an array with a length of 10 and status code 200', (done) => {
    chai.request(app)
      .get('/api/v1/blogs?news_site=planetarysociety')
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res.body.docs).to.be.an('array');
        res.body.docs.forEach(blog => {
          expect(blog.news_site).to.eql('planetarysociety')
        });
        done()
      });
  });

  it('List 5 blogs, expect it to have a length of 5 and status code 200', (done) => {
    chai.request(app)
      .get('/api/v1/blogs?limit=5')
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res.body.docs).to.be.an('array');
        expect(res.body.docs).to.have.length(5);
        done()
      });
  });

  it('Post a new blog without auth, expecting a 403 and forbidden', (done) => {
    chai.request(app)
      .post('/api/v1/blogs')
      .send({
        'news_site': 'test_site',
        'news_site_long': 'Test Site',
        'title': 'Test Blog',
        'url': 'https://spaceflightnewsapi.net',
        'featured_image': 'https://snapi.space'
      })
      .end((err, res) => {
        expect(res).to.have.status(403);
        expect(res.forbidden).eql(true);
        done()
      });
  });
});
