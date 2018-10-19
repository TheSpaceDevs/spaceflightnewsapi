process.env.NODE_ENV = 'test';

const chai = require('chai');
const chaiHttp = require('chai-http');

const should = chai.should();
const server = require('../server');

chai.use(chaiHttp);

describe('ISS', () => {
  describe('GET /iss', () => {
    it('Lists all ISS expeditions. Should be at least 1.', (done) => {
      chai.request(server)
        .get('/iss')
        .end((err, res) => {
          res.should.have.status(200);
          res.body.should.be.a('array');
          res.body.length.should.above(1);
          done();
        });
    });
  });
});