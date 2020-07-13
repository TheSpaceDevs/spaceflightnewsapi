import React, {useState, useEffect} from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

import {AppCard, LoadingComponent} from "../components";
import firebase from "../firebase";
import {ColStyle} from "../styles";

const db = firebase.firestore();

export default function Apps() {
  const [apps, setApps] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getData();
  }, []);

  const getData = () => {
    db.collection("apps").get().then((querySnapshot) => {
      setLoading(false);
      querySnapshot.forEach((app) => {
        setApps((oldArray) => [...oldArray, app.data()])
      })
    });
  };

  return (
    <Container>
      <Row className="mt-2 justify-content-center">
        <h1 className="font-weight-bold">Apps</h1>
      </Row>
      <Row>
        {loading
          ?
          <LoadingComponent/>
          :
          apps.map((app => {
            return (
              <Col lg={4} sm={6} key={app.name} style={ColStyle} >
                <AppCard app={app}
                />
              </Col>
            )
          }))
        }
      </Row>
    </Container>
  )
}
