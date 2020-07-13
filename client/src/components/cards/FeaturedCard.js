import React from 'react';
import PropTypes from 'prop-types';
import Card from "react-bootstrap/Card";

const FeatutredCard = ({title, image_url, news_site, url}) => {
  return (
    <Card style={{height: "100%"}} className="text-white text-center shadow">
      <Card.Link className="text-white font-weight-bold" href={url} target='_blank noopener noreferrer'>
      <Card.Img src={image_url} style={{height: "15rem"}}/>
      <Card.ImgOverlay className="d-flex flex-column justify-content-center">
        <Card.Title>{title}</Card.Title>
        <Card.Text>{news_site}</Card.Text>
      </Card.ImgOverlay>
      </Card.Link>
    </Card>
  );
};

FeatutredCard.propTypes = {
  title: PropTypes.string,
  image_url: PropTypes.string,
  news_site: PropTypes.string,
  url: PropTypes.string
};

export default FeatutredCard;
