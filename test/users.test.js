const chai = require('chai');
const expect = require('chai').expect;
const chaiHttp = require('chai-http');

const app = require('../app');
var token = ""

const userCredentials = {
  email: 'derk@weijers.xyz', 
  password: 'Welkom123'
}

chai.use(chaiHttp);

describe('Auth', () => {
  it('Try to list all users unauthenticated, expect a 401', (done) => {
    chai.request(app)
      .get('/api/v1/users')
      .end((err, res) => {
        expect(res).to.have.status(401);
        done()
      });
  });

  it('Authenticate, expect to get a token and status 200', (done) => {
    chai.request(app)
      .post('/api/v1/users/login')
      .send(userCredentials)
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res.body.message).to.eq("logged in")
        token = res.body.token
        done()
      });
  });


  it('Try to list all users authenticated, expect a 200', (done) => {
    chai.request(app)
      .get('/api/v1/users')
      .set('Authorization', `Bearer ${token}`)
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res.body).to.be.an('array')
        done()
      });
  });
});
