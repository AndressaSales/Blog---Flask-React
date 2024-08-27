import './Header.css';

export const Header = () => {
  return (
    <header className="header" >
      <h1>Blog Coletivo</h1>
      <p>Escreva o que quiser! Deixe sua mensagem!</p>
      <p>Escreva seu nome ou envie de forma anônima.</p>
      <p>Você escolhe!</p>
      <br />
      <p>Criado por <a href="https://www.instagram.com/omikaelbaracho/">Mikael Baracho</a> e <a href="https://www.instagram.com/andressa_salesss/">Andressa Sales</a>.</p>
      <p>Front-end e back-end respectivamente.</p>
    </header>
  );
};

export const ScrollingHeader = ({ clock }) => {
  return (
    <header className="scrolling-header">
      {clock && <p>{clock.day}/{clock.month}/{clock.year}</p>}
      <h1>Blog Coletivo</h1>
      {clock && <p>Let's talk!</p>}
    </header>
  );
};