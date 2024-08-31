import './WritingBox.css'
import PropTypes from 'prop-types';
import { useRef } from 'react';

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
// This is required on Vite Syntax
WritingBoxSwitch.propTypes = {
    isChecked: PropTypes.bool.isRequired,
    onChange: PropTypes.func.isRequired
}

export const WritingBox = ({ isChecked }) => {

    const textareaRef = useRef(null);
    const nameRef = useRef(null);

    function presentingError(field, msg) {
        field.parentNode.querySelector('.error-msg').textContent = msg
    }

    const verifyField = (fieldRef) => {
        const field = fieldRef.current

        if (!field.checkValidity()) {

            if (field.validity.valueMissing) {
                presentingError(field, `O campo não pode estar vazio.`)
            } else if (field.validity.tooLong) {
                presentingError(field, `O campo excedeu o limite de caracteres.`)
            }

        } else {
            presentingError(field, '')
        }

        console.log(field.validity)
    };

    return (
        <section className={isChecked ? 'writing-box appearing' : 'writing-box'}>
            <div className='div-input-text'>
                <textarea
                    className='input-text msg'
                    maxLength={160}
                    placeholder='Escreva sua mensagem aqui! (max: 160 caracteres)'
                    cols="30"
                    rows="5"
                    onInput={() => verifyField(textareaRef)}
                    ref={textareaRef}
                    required
                ></textarea>
                <p className='error-msg'></p>
            </div>
            <div className='div-input-text'>
                <input
                    className='input-text name'
                    placeholder='Seu nome'
                    maxLength={40}
                    type="text"
                    onInput={() => verifyField(nameRef)}
                    ref={nameRef}
                    required
                />
                <p className='error-msg'></p>
            </div>
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
WritingBox.propTypes = {
    isChecked: PropTypes.bool.isRequired
}