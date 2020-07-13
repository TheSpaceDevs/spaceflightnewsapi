import React from 'react';
import Spinner from "react-bootstrap/Spinner";
import Col from "react-bootstrap/Col";

const LoadingComponent = () => {
  return (
    <Col className="col-12 text-center mt-4">
      <Spinner animation="border"/>
    </Col>
  );
};

export default LoadingComponent;
