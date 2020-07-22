import React, { useState, useEffect } from 'react';
import { Container, Form, Col, Row, Button, Alert } from 'react-bootstrap';
import { withRouter } from 'react-router';
import axios from 'axios';
import AuthService from '../services/AuthService';

const ArticleEntry = ({ history }) => {
  const [newsArticle, setNewArticle] = useState({
    title: '',
    newsSite: '',
    url: '',
    publishedAt: '',
    imageUrl: '',
    summary: '',
    featured: false,
    launches: [],
    events: [],
  });
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState({ visible: false, message: '' });
  const [upcomingLaunches, setUpcomingLaunches] = useState([]);
  const [upcomingEvents, setUpcomingEvents] = useState([]);

  useEffect(() => {
    // Call sync to be sure that the token is still valid before sending an article
    AuthService.sync();
    getLaunchesAndEvents();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSaving(true);


    // Getting and setting the IDs of the events that were selected

    // Saving the article
    try {
      await axios.post('/v2/articles', { ...newsArticle });
      history.push('/admin');
    } catch (e) {
      setSaving(false);
      if (e.response && e.response.status === 422) {
        console.log("hier");
        return setError({ ...error, visible: true, message: 'Please check the form for errors and make sure the title and url are unique' });
      }
      console.log("daar");
      setError({ ...error, visible: true, message: 'Please contact Derk and tell him what you broke' });
    }
  };

  const getLaunchesAndEvents = async () => {
    const launchResult = await axios.get('https://spacelaunchnow.me/api/3.5.0/launch/upcoming?limit=10');
    setUpcomingLaunches(launchResult.data.results);

    const eventsResult = await axios.get('https://spacelaunchnow.me/api/3.5.0/event/upcoming?limit=10');
    setUpcomingEvents(eventsResult.data.results);
  };

  // Handle the multi select form part for the launches
  const handleLaunchSelect = (e) => {
    let ids = Array.from(e.target.selectedOptions, option => option.id);

    const selectedLaunches = [];
    ids.forEach((id) => {
      selectedLaunches.push({ provider: 'Space Launch Now', id: id });
    });
    setNewArticle({ ...newsArticle, launches: selectedLaunches });
  };

  // Handle the multi select form part for the events
  const handleEventSelect = (e) => {
    let ids = Array.from(e.target.selectedOptions, option => option.id);

    const selectedEvents = [];
    ids.forEach((id) => {
      selectedEvents.push({ provider: 'Space Launch Now', id: id });
    });
    setNewArticle({ ...newsArticle, events: selectedEvents });
  };

  return (
    <Container>
      <Form className="mt-2" onSubmit={(e) => handleSubmit(e)}>
        <Row>
          <Col>
            <Alert show={error.visible} variant="danger">{error.message}</Alert>
          </Col>
        </Row>
        <Row>
          <Col>
            <Form.Label>
              Title
            </Form.Label>
            <Form.Control type="text" onChange={(e) => setNewArticle({ ...newsArticle, title: e.target.value })}/>
          </Col>
          <Col>
            <Form.Label>
              News Site
            </Form.Label>
            <Form.Control type="text" onChange={(e) => setNewArticle({ ...newsArticle, newsSite: e.target.value })}/>
          </Col>
        </Row>
        <Row>
          <Col>
            <Form.Label>
              Article URL
            </Form.Label>
            <Form.Control type="text" onChange={(e) => setNewArticle({ ...newsArticle, url: e.target.value })}/>
          </Col>
          <Col>
            <Form.Label>
              Date Published (date of article)
            </Form.Label>
            <Form.Control type="datetime-local"
                          onChange={(e) => setNewArticle({ ...newsArticle, publishedAt: e.target.value })}/>
          </Col>
          <Col>
            <Form.Label>
              Image URL
            </Form.Label>
            <Form.Control type="text" onChange={(e) => setNewArticle({ ...newsArticle, imageUrl: e.target.value })}/>
          </Col>
        </Row>
        <Row>
          <Col>
            <Form.Label>Summary</Form.Label>
            <Form.Control as="textarea" rows="3"
                          onChange={(e) => setNewArticle({ ...newsArticle, summary: e.target.value })}/>
          </Col>
        </Row>
        <Row>
          <Col>
            <Form.Check type="checkbox" label="Featured"
                        onChange={() => setNewArticle({ ...newsArticle, featured: !newsArticle.featured })}/>
          </Col>
        </Row>
        <Row className="mt-3">
          <Col>
            <Form.Control as="select" multiple htmlSize={10} onChange={(e) => handleLaunchSelect(e)}>
              {
                upcomingLaunches.map((launch) => {
                  return <option key={launch.id} id={launch.id}>{launch.name}</option>;
                })
              }
            </Form.Control>
          </Col>
          <Col>
            <Form.Control as="select" multiple htmlSize={10} onChange={(e) => handleEventSelect(e)}>
              {
                upcomingEvents.map((event) => {
                  return <option key={event.id} id={event.id}>{event.name}</option>;
                })
              }
            </Form.Control>
          </Col>
        </Row>
        <Row className="mt-2">
          <Col>
            <Button disabled={saving} type="submit">Save</Button>
          </Col>
        </Row>
      </Form>
    </Container>
  );
};

export default withRouter(ArticleEntry);
