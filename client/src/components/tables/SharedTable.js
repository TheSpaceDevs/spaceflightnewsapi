import React from 'react';
import { Table } from 'react-bootstrap';

const SharedTable = ({ data }) => {
  const RenderData = () => {
    return data.map((article) => {
      return (
        <tr key={article._id} style={{cursor: 'pointer'}}>
          <td>{article.title}</td>
          <td>{article.newsSite}</td>
          <td>{article.publishedAt}</td>
        </tr>
      );
    });
  };

  return (
    <Table striped bordered hover size="sm">
      <thead>
      <tr>
        <th>Title</th>
        <th>News Site</th>
        <th>Published</th>
      </tr>
      </thead>
      <tbody>
      <RenderData/>
      </tbody>
    </Table>
  );
};

export default SharedTable;