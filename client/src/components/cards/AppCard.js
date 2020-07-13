import React from 'react';
import Card from "react-bootstrap/Card";
import Badge from "react-bootstrap/Badge";

const AppCard = (props) => {
  const {name, website, discord, supporter, image, android_url, ios_url} = props.app;

  // Check if the app is a supporter
  const _supporterBadge = () => {
    if (supporter) {
      return (
        <div className="text-center">
          <Badge pill variant="success">Patreon Supporter</Badge>
        </div>
      )
    } else {
      return (
        <div style={{height: 24}}/>
      )
    }
  };

  // Check if Discord needs to be rendered
  const _discordLink = () => {
    if (discord) {
      return <Card.Link href={discord} target='_blank noopener noreferrer'>Discord</Card.Link>
    }
  };

  // Check if Android link needs to rendered
  const _androidLink = () => {
    if (android_url) {
      return <Card.Link href={android_url} target='_blank noopener noreferrer'>Android</Card.Link>
    }
  };

  // Check if the iOS link needs to be rendered
  const _iosLink = () => {
    if (ios_url) {
      return <Card.Link href={ios_url} target='_blank noopener noreferrer'>iOS</Card.Link>
    }
  };

  return (
    <div>
      {/*Render the card with a shadow behind it*/}
      <Card style={styles.cardStyle} className="shadow">
        <Card.Body>
          <Card.Img style={styles.imageStyle} src={image} className="rounded-circle mx-auto d-block shadow-sm"/>
          <Card.Title style={styles.cardTitleStyle} className="text-center">{name}</Card.Title>

          {/*Render supporter badge if applicable*/}
          {_supporterBadge()}

          {/*Render the links*/}
          <div className="text-center">
            <Card.Link href={website} target='_blank noopener noreferrer'>Website</Card.Link>
            {_discordLink()}
            {_androidLink()}
            {_iosLink()}
          </div>
        </Card.Body>
      </Card>
    </div>
  );
};

const styles = {
  cardStyle: {
    marginTop: 5
  },
  cardTitleStyle: {
    marginTop: 10,
    marginBottom: 5
  },
  imageStyle: {
    height: 150,
    width: 150
  }
};

export default AppCard;
