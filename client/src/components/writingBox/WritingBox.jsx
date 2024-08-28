import './WritingBox.css'

export const WritingBoxSwitch = ({ isChecked, onChange }) => {
    return (
        <div className='writing-box-switch'>
            <input checked={isChecked} onChange={onChange} type="checkbox" id="checkbox" />
                <label htmlFor="checkbox" className="toggle">
                    <div className="bars" id="bar1"></div>
                    <div className="bars" id="bar2"></div>
                    <div className="bars" id="bar3"></div>
                </label>
        </div>
    )
}

export const WritingBox = ({ isChecked }) => {
    return (
        <section className={isChecked ? 'writing-box appearing' : 'writing-box'} >
            <textarea className='input-text msg' maxLength={160} placeholder='Escreva sua mensagem aqui! (max: 160 caracteres)' cols="30" rows="5"></textarea>
            <input className='input-text name' placeholder='Seu nome' maxLength={40} type="text" />
            <button className='send-button'>
                <div className="svg-wrapper-1">
                    <div className="svg-wrapper">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
                            <path fill="none" d="M0 0h24v24H0z"></path>
                            <path fill="currentColor" d="M1.946 9.315c-.522-.174-.527-.455.01-.634l19.087-6.362c.529-.176.832.12.684.638l-5.454 19.086c-.15.529-.455.547-.679.045L12 14l6-8-8 6-8.054-2.685z"></path>
                        </svg>
                    </div>
                </div>
                <span>Send</span>
            </button>
        </section>
    )
}