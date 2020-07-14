import React from 'react';
import {Container, Tabs, Tab} from 'react-bootstrap';
import {ArticleTable} from './index';

const AdminDashboard = () => {
  return (
    <Container>
      <Tabs defaultActiveKey="articles">
        <Tab eventKey="articles" title="Articles">
          <ArticleTable />
        </Tab>
        <Tab eventKey="blogs" title="Blogs">
          Blogs
        </Tab>
        <Tab eventKey="reports" title="Reports">
          Reports
        </Tab>
        <Tab eventKey="users" title="Users">
          Users
        </Tab>
        <Tab eventKey="images" title="Images" disabled />
        <Tab eventKey="videos" title="Videos" disabled />
      </Tabs>
    </Container>
  );
};

export default AdminDashboard;