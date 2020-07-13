import React, {useState, useEffect} from "react";
import axios from "axios";
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

import {NewsCard, LoadingComponent} from "../components";
import {ColStyle} from "../styles";

function LatestNewsComponent() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getData();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const getData = async () => {
    try {
      const results = await axios.get(
        `https://spaceflightnewsapi.net/api/v1/articles?limit=6`
      );
      setData(results.data);
      setLoading(false)
    } catch (e) {
      console.log(e)
    }
  };

  return (
    <>
      <Row className="mt-2 justify-content-center">
        <h1 className="font-weight-bold">Latest News</h1>
      </Row>
      <Row>
        {loading
          ?
          <LoadingComponent/>
          :
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
        }
      </Row>
    </>
  )
}

export default LatestNewsComponent;
