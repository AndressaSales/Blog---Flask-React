import './WritingBox.css'

export const WritingBox = () => {

    return (
        <section className='writing-box'>
            <textarea className='input-text msg' maxLength={160} placeholder='Escreva sua mensagem aqui! (max: 160 caracteres)' cols="30" rows="5"></textarea>
            <input className='input-text name' placeholder='Seu nome' maxLength={40} type="text" />
            <button class="button">
                Share
            </button>
        </section>
    )
}