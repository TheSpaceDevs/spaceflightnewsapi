import React, {useState, useEffect} from "react";
import axios from "axios";
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

import {NewsCard, LoadingComponent, PaginateComponent} from "../components";
import {ColStyle} from "../styles";
import Container from "react-bootstrap/Container";

function NewsComponent() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [page, setPage] = useState(0);

  useEffect(() => {
    getData();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [page]);

  const getData = async () => {
    try {
      const results = await axios.get(
        `https://spaceflightnewsapi.net/api/v1/articles?limit=21&page=${page}`
      );
      setData(results.data);
      setLoading(false)
    } catch (e) {
      console.log(e)
    }
  };

  return (
    <Container>
      <Row className="mt-2 justify-content-center">
        <h1 className="font-weight-bold">News</h1>
      </Row>
      <Row>
        {loading
          ?
          <LoadingComponent/>
          :
          <div>
            <Row>
              {data.docs.map(article => {
                return (
                  <Col style={ColStyle} xl={4} lg={4} sm={6} key={article._id} >
                    <NewsCard
                      title={article.title}
                      site={article.news_site_long}
                      url={article.url}
                      date={article.published_date}
                      image={article.featured_image}
                    />
                  </Col>
                );
              })}
            </Row>
            <Row>
              <Col>
                <PaginateComponent
                  totalPages={data.totalPages}
                  setPage={setPage}
                />
              </Col>
            </Row>
          </div>
        }
      </Row>
    </Container>
  )
}

export default NewsComponent;
