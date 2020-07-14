import React, {useState, useEffect} from 'react';
import {Table} from 'react-bootstrap';
import axios from 'axios';
import {SharedTable} from './index';

const ArticleTable = () => {
  const [articles, setArticles] = useState([])

  useEffect(() => {
    getArticles()
  }, [])

  const getArticles = async () => {
    const articles = await axios.get('/v2/articles')
    setArticles(articles.data.docs)
  }


  return (
    <SharedTable data={articles} />
  );
};

export default ArticleTable;