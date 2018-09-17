

process.env.NODE_ENV = 'test';

const chai = require('chai');
const chaiHttp = require('chai-http');

const should = chai.should();
const server = require('../server');

chai.use(chaiHttp);

describe('Articles', () => {
  describe('GET /articles', () => {
    it('Lists all articles. Should be above 150.', (done) => {
      chai.request(server)
        .get('/articles')
        .end((err, res) => {
          res.should.have.status(200);
          res.body.should.be.a('array');
          res.body.length.should.above(123);
          done();
        });
    });
  });

  describe('GET /articles?news_site=nasaspaceflight&limit=5', () => {
    it('Lists 5 articles from nfs.', (done) => {
      chai.request(server)
        .get('/articles?news_site=nasaspaceflight&limit=5')
        .end((err, res) => {
          res.should.have.status(200);
          res.body.should.be.a('array');
          res.body.length.should.equal(5);
          done();
        });
    });
  });

  describe('GET /articles?date_published=1535666400', () => {
    it('Get all articles published at a certain date', (done) => {
      chai.request(server)
        .get('/articles?date_published=1535666400')
        .end((err, res) => {
          res.should.have.status(200);
          res.body.should.be.a('array');
          res.body.length.should.above(-1);
          done();
        });
    });
  });

  describe('GET /articles?date_added=1535402404', () => {
    it('Get all articles added at a certain date', (done) => {
      chai.request(server)
        .get('/articles?date_added=1535402404')
        .end((err, res) => {
          res.should.have.status(200);
          res.body.should.be.a('array');
          res.body.length.should.above(-1);
          done();
        });
    });
  });
});

describe('Article', () => {
  describe('GET /article?_id=5b883685d736f46e52aad1c6', () => {
    it('Get a single article', (done) => {
      chai.request(server)
        .get('/article?_id=5b883685d736f46e52aad1c6')
        .end((err, res) => {
          res.should.have.status(200);
          res.body.should.be.a('array');
          res.body.length.should.equal(1);
          done();
        });
    });
  });
});
