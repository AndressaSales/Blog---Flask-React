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
          <br />  
        </header>
      );
};

export const ScrollingHeader = () => {
    return (
        <header className="scrolling-header">
          <h1>Blog Coletivo</h1>
        </header>
    );
};