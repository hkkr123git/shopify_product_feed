import React from 'react';
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import AddFeed from './screens/add-feed/add-feed';
import Layout from './components/layout/layout';
import './App.css';

function App() {
  return (
    <Router>
      <Layout>
        <Switch>
          <Route path="/" exact component={AddFeed} />
        </Switch>
      </Layout>
    </Router>
  );
}

export default App;
