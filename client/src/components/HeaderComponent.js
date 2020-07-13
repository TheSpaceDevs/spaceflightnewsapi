import React, {useState, useEffect} from 'react'
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import { Link, useLocation } from 'react-router-dom';
import NavDropdown from "react-bootstrap/NavDropdown";
import axios from 'axios';
import Button from "react-bootstrap/Button";
import Badge from "react-bootstrap/Badge";

export default function HeaderComponent() {
  const [version, setVersion] = useState('');
  const {pathname} = useLocation();

  useEffect(() => {
    getVersion();
  });

  const getVersion = async () => {
    const result = await axios.get('https://spaceflightnewsapi.net/api/v1/info');
    setVersion(result.data.api_version);
  };

  return (
    <Navbar bg="primary" variant="dark" expand="lg">
      <Navbar.Brand as={Link} to="/">Spaceflight News API</Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="mr-auto">
          <Nav.Link as={Link} active={pathname === "/news"} to="/news">News</Nav.Link>
          <Nav.Link as={Link} active={pathname === "/blogs"} to="/blogs">Blogs</Nav.Link>
          <Nav.Link as={Link} active={pathname === "/reports"} to="/reports">Reports</Nav.Link>
          <Nav.Link as={Link} active={pathname === "/apps"} to="/apps">Apps</Nav.Link>
          <Nav.Link as={Link} to="/about">About</Nav.Link>
        </Nav>
        <Nav>
          <Button
            variant="primary"
            onClick={() => {
              window.open('https://github.com/spaceflightnewsapi/spaceflightnewsapi/blob/master/README.md#changelog', '_blank noopener noreferrer')
            }}
          >
            API Version <Badge variant="light">{version}</Badge>
            <span className="sr-only">unread messages</span>
          </Button>
          <Nav.Link active href="https://spaceflightnewsapi.net/api/v1/" target='_blank noopener noreferrer' >API Docs</Nav.Link>
          <NavDropdown active title="Connect" id="basic-nav-dropdown">
            <NavDropdown.Item href="https://discord.gg/PhvsBHP" target='_blank noopener noreferrer'>Discord</NavDropdown.Item>
            <NavDropdown.Item href="https://www.reddit.com/r/snapi/" target='_blank noopener noreferrer'>Reddit</NavDropdown.Item>
            <NavDropdown.Item href="https://twitter.com/the_snapi" target='_blank noopener noreferrer'>Twitter</NavDropdown.Item>
            <NavDropdown.Item href="https://github.com/spaceflightnewsapi" target='_blank noopener noreferrer'>GitHub</NavDropdown.Item>
          </NavDropdown>
          <Nav.Link active href="https://discordapp.com/oauth2/authorize?client_id=598493983886540800&scope=bot&permissions=2048" target='_blank noopener noreferrer' >Discord Bot</Nav.Link>
          <Nav.Link active href="https://www.patreon.com/bePatron?u=8565105" target='_blank noopener noreferrer' >Patreon</Nav.Link>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  )
}
