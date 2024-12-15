import React, { useState, useRef } from 'react';
import axios from 'axios';

const Chat = () => {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState('');
    const printRef = useRef();

    const sendMessage = async () => {
        if (input.trim() === '') return;

        const userMessage = { sender: 'user', text: input };
        setMessages([...messages, userMessage]);

        try {
            const response = await axios.post('http://localhost:5000/chat', { message: input });
            const botMessage = { sender: 'bot', text: response.data.response };
            setMessages([...messages, userMessage, botMessage]);
        } catch (error) {
            console.error('Error sending message:', error);
        }

        setInput('');
    };

    const clearChat = () => {
        setMessages([]);
    };

    const printChat = () => {
        const printContent = printRef.current.innerHTML;
        const originalContent = document.body.innerHTML;
        document.body.innerHTML = `
            <div>
                <h1>Shop Name</h1>
                <p>Shop Address</p>
                <p>Contact Information</p>
                <hr />
                ${printContent}
            </div>
        `;
        window.print();
        document.body.innerHTML = originalContent;
        window.location.reload();
    };

    return (
        <div className="flex flex-col h-screen max-w-md mx-auto border border-gray-300 rounded-lg overflow-hidden shadow-lg bg-gray-100">
            <div className="flex-1 p-4 overflow-y-auto bg-white" ref={printRef}>
                {messages.map((msg, index) => (
                    <div key={index} className={`mb-4 p-2 rounded-lg ${msg.sender === 'user' ? 'bg-green-200 self-end' : 'bg-gray-200 self-start'}`}>
                        {msg.text}
                    </div>
                ))}
            </div>
            <div className="flex p-4 border-t border-gray-300 bg-gray-100">
                <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    onKeyDown={(e) => e.key === 'Enter' && sendMessage()}
                    className="flex-1 p-2 border border-gray-300 rounded-lg mr-2"
                    placeholder="Type product name..."
                />
                <button onClick={sendMessage} className="p-2 bg-blue-500 text-white rounded-lg mr-2">Send</button>
                <button onClick={clearChat} className="p-2 bg-red-500 text-white rounded-lg mr-2">Clear Chat</button>
                <button onClick={printChat} className="p-2 bg-green-500 text-white rounded-lg">Print Chat</button>
            </div>
        </div>
    );
};

export default Chat;
