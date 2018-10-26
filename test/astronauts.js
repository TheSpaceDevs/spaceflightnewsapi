process.env.NODE_ENV = 'test';

const chai = require('chai');
const chaiHttp = require('chai-http');

const should = chai.should();
const server = require('../server');

chai.use(chaiHttp);

describe('Astronauts', () => {
  describe('GET /astronauts', () => {
    it('Lists all astronauts.', (done) => {
      chai.request(server)
        .get('/astronauts')
        .end((err, res) => {
          res.should.have.status(200);
          res.body.should.be.a('array');
          done();
        });
    });
  });
});