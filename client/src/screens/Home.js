import React from "react";
import Container from "react-bootstrap/Container";
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

import { LatestNewsComponent, FeaturedNewsComponent } from "../components";

function Home(props) {
  return (
    <Container>
      <Row className="row-eq-height">
        <Col>
          <FeaturedNewsComponent />
          <hr />
          <LatestNewsComponent />
        </Col>
      </Row>
    </Container>
  )
}

export default Home;
