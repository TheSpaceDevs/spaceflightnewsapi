import React from "react";
import Card from "react-bootstrap/Card";

function NewsCard(props) {
  const {title, site, url, date, image} = props;

  return (
    <Card style={{height: "100%"}} className='shadow'>
      <Card.Img variant="top" src={image} style={{height: "15rem"}}/>
      <Card.Body>
        <Card.Title><a href={url} target='_blank noopener noreferrer'>{title}</a></Card.Title>
        <Card.Subtitle className="mb-2 text-muted">{`${site} | ${new Date(date).toLocaleDateString()}`}</Card.Subtitle>
      </Card.Body>
    </Card>
  );
}

export default NewsCard;