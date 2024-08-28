import { useState } from 'react';
import './App.css';
import { Header, ScrollingHeader } from './components/header/Header.jsx'
import { WritingBoxSwitch, WritingBox } from './components/writingBox/WritingBox.jsx'
import getCurrentDateTime from './scripts/clock.js'

function App() {
  const paragraphs = [];

  for (let i = 0; i < 100; i++) {
    paragraphs.push(<p key={i}>{i}</p>);
  }

  const [writingBoxSwitchIsChecked, setWritingBoxSwitchIsChecked] = useState(false)

  return (
    <div className="App">
      <div className='main-page'>
        <ScrollingHeader clock={getCurrentDateTime()} />
        <Header />

        <section className='dialogue-section'>
          <WritingBoxSwitch isChecked={writingBoxSwitchIsChecked} onChange={() => setWritingBoxSwitchIsChecked(!writingBoxSwitchIsChecked)} />
          <WritingBox isChecked={writingBoxSwitchIsChecked} />
          {paragraphs}
        </section>
      </div>
    </div>
  );
}

export default App;
