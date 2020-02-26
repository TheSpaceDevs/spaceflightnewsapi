const chai = require('chai');
const expect = require('chai').expect;
const chaiHttp = require('chai-http');

const app = require('../app');

chai.use(chaiHttp);

describe('Reports', () => {
  it('List all reports, expect it to have a length of 10 and status code 200', (done) => {
    chai.request(app)
      .get('/api/v1/reports')
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res.body.docs).to.be.an('array');
        expect(res.body.docs).to.have.length(10);
        done()
      });
  });

  it('List all reports on the second page, expect it to have a length of 10 and status code 200', (done) => {
    chai.request(app)
      .get('/api/v1/reports?page=2')
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res.body.docs).to.be.an('array');
        expect(res.body.docs).to.have.length(10);
        done()
      });
  });

  it('Get a single report, expect it to be an array with a length of 10 and status code 200', (done) => {
    chai.request(app)
      .get('/api/v1/reports?_id=5dcbe09cb851c292ff6b108a')
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res.body.docs).to.be.an('array');
        expect(res.body.docs).to.have.length(1);
        done()
      });
  });

  it('List 5 reports, expect it to have a length of 5 and status code 200', (done) => {
    chai.request(app)
      .get('/api/v1/reports?limit=5')
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res.body.docs).to.be.an('array');
        expect(res.body.docs).to.have.length(5);
        done()
      });
  });
});
