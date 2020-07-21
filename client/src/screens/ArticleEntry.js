import React, { useState } from 'react';
import { Container, Form, Col, Row, Button, Alert } from 'react-bootstrap';
import { withRouter } from 'react-router';
import axios from 'axios';

const ArticleEntry = ({ history }) => {
  const [newsArticle, setNewArticle] = useState({
    title: '',
    newsSite: '',
    url: '',
    publishedAt: "",
    imageUrl: '',
    summary: '',
    featured: false,
  });
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState({ visible: false, message: '' });

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSaving(true);
    try {
      await axios.post('/v2/articles', { ...newsArticle });
      history.push("/admin");
    } catch (e) {
      setSaving(false);
      if (e.response && e.response.status === 422) {
        setError({ ...error, visible: true, message: 'Please check the forms for errors' });
      }
      setError({ ...error, visible: true, message: 'Please contact Derk and tell him what you broke' });
    }

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
                        onChange={(e) => setNewArticle({ ...newsArticle, featured: !newsArticle.featured })}/>
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
