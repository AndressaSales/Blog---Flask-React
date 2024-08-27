import './App.css';
import { Header, ScrollingHeader } from './components/header/Header.jsx'
import getCurrentDateTime from './scripts/clock.js'

function App() {
  const paragraphs = [];

  for (let i = 0; i < 100; i++) {
    paragraphs.push(<p key={i}>{i}</p>);
  }

  return (
    <div className="App">
      <ScrollingHeader clock={getCurrentDateTime()} />
      <Header />

      {paragraphs}
    </div>
  );
}

export default App;
