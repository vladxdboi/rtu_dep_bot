const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');

const app = express();
const PORT = process.env.PORT || 3000;

// Replace with your bot token
const TOKEN = '7911027827:AAFmPaq8pUdQSjKOASuMAgrTd9001raAtJ4';
const TELEGRAM_API_URL = `https://api.telegram.org/bot${TOKEN}/`;

// Middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Webhook endpoint
app.post('/webhook', async (req, res) => {
    const message = req.body.message;

    if (message) {
        const chatId = message.chat.id;
        const text = message.text;

        // Respond with a simple echo
        await sendMessage(chatId, `You said: ${text}`);
    }

    res.sendStatus(200);
});

// Function to send a message
const sendMessage = async (chatId, text) => {
    try {
        await axios.post(`${TELEGRAM_API_URL}sendMessage`, {
            chat_id: chatId,
            text: text,
        });
    } catch (error) {
        console.error('Error sending message:', error);
    }
};

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});