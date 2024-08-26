import './Header.css';
import { useEffect, useRef } from 'react';

export const Header = () => {
    // Cria uma referência ao elemento de cabeçalho usando o useRef
    const headerRef = useRef(null);
  
    // Executa um efeito após o componente ser montado
    useEffect(() => {
      // Obtém a referência ao elemento de cabeçalho
      const header = headerRef.current;
  
      // Define a função de tratamento de rolagem
      const handleScroll = () => {
        // Obtém a posição de rolagem vertical da janela
        const scrollY = window.scrollY;
  
        // Obtém a altura do cabeçalho
        const headerHeight = header.offsetHeight;
  
        // Verifica se o usuário rolou além da altura do cabeçalho
        if (scrollY > 0.1) {
          // Adiciona a classe "scrolling" ao cabeçalho
          header.classList.add('scrolling');
        } else {
          // Remove a classe "scrolling" do cabeçalho
          header.classList.remove('scrolling');
        }
      };
  
      // Adiciona o listener para o evento de rolagem
      window.addEventListener('scroll', handleScroll);
  
      // Retorna uma função de limpeza para remover o listener quando o componente for desmontado
      return () => window.removeEventListener('scroll', handleScroll);
    }, []);
  

  return (
    <header className="header" ref={headerRef}>
      <h1>Blog Coletivo</h1>
    </header>
  );
};