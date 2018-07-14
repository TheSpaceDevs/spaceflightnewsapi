'use strict';

process.env.NODE_ENV = 'test';

let chai = require('chai');
let chaiHttp = require('chai-http');
let should = chai.should();
let errors = require('../controllers/errors');
let server = require('../server');

describe('Errors', () => {

  describe('newHttpError', () => {

    it('creates a new error', (done) => {
      let err = errors.newHttpError(401, 'unauthorized');
      err.message.should.equal('unauthorized');
      err.status.should.equal(401);
      done();
    });

    it('creates a new error without status', (done) => {
      let errStatusNull = errors.newHttpError(null, 'status is null');
      let errStatusUndefined = errors.newHttpError(undefined, 'status is undefined');
      errStatusNull.message.should.equal('status is null');
      errStatusUndefined.message.should.equal('status is undefined');
      should.not.exist(errStatusNull.status);
      should.not.exist(errStatusUndefined.status);
      done();
    });

    it('creates a new error without message', (done) => {
      let errMessageNull = errors.newHttpError(403, null);
      let errMessageUndefined = errors.newHttpError(418);
      errMessageNull.status.should.equal(403);
      errMessageUndefined.status.should.equal(418);

      // By default, if you don't pass in a message to a new Error, the
      // message becomes an empty string
      errMessageNull.message.should.equal('');
      errMessageUndefined.message.should.equal('');

      done();
    });

  });

  describe('Null Route', () => {
    it('returns a 404 response', (done) => {
      chai.request(server)
        .get('/nonexistentroute')
        .end((err, res) => {
          res.should.have.status(404);
          res.body.should.be.a('object');
          res.body.message.should.equal('not found');
          done();
        });
    });
  });

});
