process.env.NODE_ENV = 'test';

const chai = require('chai');
const chaiHttp = require('chai-http');

const should = chai.should();
const server = require('../server');

chai.use(chaiHttp);

describe('mannedflights', () => {
  describe('GET /mannedflights', () => {
    it('Lists all manned flights.', (done) => {
      chai.request(server)
        .get('/mannedflights')
        .end((err, res) => {
          res.should.have.status(200);
          res.body.should.be.a('array');
          res.body.length.should.above(1);
          done();
        });
    });
  });
});