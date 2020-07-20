import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Button } from 'react-bootstrap';
import {withRouter} from 'react-router';
import { SharedTable } from './index';

const ArticleTable = ({history}) => {
  const [articles, setArticles] = useState([]);

  useEffect(() => {
    getArticles();
  }, []);

  const getArticles = async () => {
    const articles = await axios.get('/v2/articles');
    setArticles(articles.data.docs);
  };


  return (
    <>
      <SharedTable data={articles}/>
      <Button onClick={() => history.push('/admin/article/new')}>Add</Button>
    </>
  );
};

export default withRouter(ArticleTable);