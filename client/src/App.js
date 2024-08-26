import './App.css';
import { Header, ScrollingHeader } from './components/header/Header.jsx'

function App() {
  const paragraphs = [];

  for (let i = 0; i < 100; i++) {
    paragraphs.push(<p key={i}>{i}</p>);
  }

  return (
    <div className="App">
      <ScrollingHeader />
      <Header />
      {paragraphs}
    </div>
  );
}

export default App;
