import React, { useState, useEffect } from 'react';
import { Container, Form, Col, Row, Button, Alert } from 'react-bootstrap';
import { withRouter } from 'react-router';
import axios from 'axios';
import _ from 'lodash';
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
  const [launchSearch, setLaunchQuery] = useState('');
  const [eventSearch, setEventQuery] = useState('');
  const [validated, setValidated] = useState(false);

  useEffect(() => {
    // Call sync to be sure that the token is still valid before sending an article
    AuthService.sync();
  }, []);

  useEffect(() => {
    // Call sync to be sure that the token is still valid before sending an article
    getLaunches();
  }, [launchSearch]);

  useEffect(() => {
    // Call sync to be sure that the token is still valid before sending an article
    getEvents();
  }, [eventSearch]);

  // Handle saving the article
  const handleSubmit = async (e) => {
    e.preventDefault();
    setSaving(true);
    const form = e.currentTarget;
    if (form.checkValidity() === true) {
      try {
        await axios.post('/v2/articles', { ...newsArticle });
        history.push('/admin');
      } catch (e) {
        setSaving(false);
        if (e.response && e.response.status === 422) {
          return setError({
            ...error,
            visible: true,
            message: 'Please check the form for errors and make sure the title and url are unique',
          });
        }
        setError({ ...error, visible: true, message: 'Please contact Derk and tell him what you broke' });
      }
    }
    setSaving(false);
    setValidated(true);
  };

  // Function to get the launches
  // Is retrigered once a search query is provided
  const getLaunches = async () => {
    try {
      const launchResult = await axios.get(`https://spacelaunchnow.me/api/3.5.0/launch/upcoming?limit=10&search=${launchSearch}`);
      setUpcomingLaunches(launchResult.data.results);
    } catch (e) {
      alert('There was an error getting the launches and events');
    }
  };

  // Function to get the launches
  // Is retrigered once a search query is provided
  const getEvents = async () => {
    try {
      const eventsResult = await axios.get(`https://spacelaunchnow.me/api/3.5.0/event/upcoming?limit=10&search=${eventSearch}`);
      setUpcomingEvents(eventsResult.data.results);
    } catch (e) {
      alert('There was an error getting the launches and events');
    }
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

  // Handle searches
  const handleSearch = _.debounce((query, type) => {
    if (type === 'launch') {
      setLaunchQuery(query);
    }

    if (type === 'event') {
      setEventQuery(query);
    }
  }, 800);

  return (
    <Container>
      <Form noValidate validated={validated} className="mt-2" onSubmit={(e) => handleSubmit(e)}>
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
            <Form.Control required type="text"
                          onChange={(e) => setNewArticle({ ...newsArticle, title: e.target.value })}/>
            <Form.Control.Feedback type="invalid">
              This cannot be empty
            </Form.Control.Feedback>
          </Col>
          <Col>
            <Form.Label>
              News Site
            </Form.Label>
            <Form.Control required type="text"
                          onChange={(e) => setNewArticle({ ...newsArticle, newsSite: e.target.value })}/>
            <Form.Control.Feedback type="invalid">
              This cannot be empty
            </Form.Control.Feedback>
          </Col>
        </Row>
        <Row>
          <Col>
            <Form.Label>
              Article URL
            </Form.Label>
            <Form.Control required type="text"
                          onChange={(e) => setNewArticle({ ...newsArticle, url: e.target.value })}/>
            <Form.Control.Feedback type="invalid">
              This cannot be empty
            </Form.Control.Feedback>
          </Col>
          <Col>
            <Form.Label>
              Date Published (date of article)
            </Form.Label>
            <Form.Control required type="datetime-local"
                          onChange={(e) => setNewArticle({ ...newsArticle, publishedAt: e.target.value })}/>
            <Form.Control.Feedback type="invalid">
              This cannot be empty
            </Form.Control.Feedback>
          </Col>
          <Col>
            <Form.Label>
              Image URL
            </Form.Label>
            <Form.Control required type="text" onChange={(e) => setNewArticle({ ...newsArticle, imageUrl: e.target.value })}/>
            <Form.Control.Feedback type="invalid">
              This cannot be empty
            </Form.Control.Feedback>
          </Col>
        </Row>
        <Row>
          <Col>
            <Form.Label>Summary</Form.Label>
            <Form.Control required as="textarea" rows="3"
                          onChange={(e) => setNewArticle({ ...newsArticle, summary: e.target.value })}/>
            <Form.Control.Feedback type="invalid">
              This cannot be empty
            </Form.Control.Feedback>
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
            <Form.Label>Upcoming Launches</Form.Label>
            <Form.Control type="text" placeholder="Search..." onChange={(e) => handleSearch(e.target.value, 'launch')}/>
            <Form.Control as="select" multiple htmlSize={10} onChange={(e) => handleLaunchSelect(e)}>
              {
                upcomingLaunches.map((launch) => {
                  return <option key={launch.id} id={launch.id}>{launch.name}</option>;
                })
              }
            </Form.Control>
          </Col>
          <Col>
            <Form.Label>Upcoming Events</Form.Label>
            <Form.Control type="text" placeholder="Search..." onChange={(e) => handleSearch(e.target.value, 'event')}/>
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
