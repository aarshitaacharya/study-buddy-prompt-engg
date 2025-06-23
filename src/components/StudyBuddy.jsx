import React, { useState } from 'react'
import { Send, BookOpen, Brain, MessageSquare } from 'lucide-react';

function StudyBuddy() {
    const [messages, setMessages] = useState([
        {
            id: 1,
            type: 'system',
            content: 'Hi! I\'m your Study Buddy. I can help you learn using different teaching techniques. What would you like to study today?'
        }
    ])

    const [inputText, setInputText] = useState('');
    const [isLoading, setLoading] = useState(false);

    const handleSubmit = async (e) => {
        if(!inputText.trim()) return;

        const userMessage = {
            id: Date.now(),
            type: 'user',
            content: inputText
        }

        setMessages(prev => [...prev, userMessage]);
        setInputText('');
        setLoading(true);

        // temp response

        setTimeout(()=> {
            const aiMessage = {
                id: Date.now() + 1,
                type: 'assistant',
                content: `I understand you want to learn about: "${inputText}". This is placeholder text, I am working on the functionality.`
            }
            setMessages(prev => [...prev, aiMessage]);
            setLoading(false);
        }, 1000)     
    }


  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="container mx-auto px-4 py-8 max-w-4xl">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="flex items-center justify-center gap-2 mb-4">
            <Brain className="w-8 h-8 text-indigo-600" />
            <h1 className="text-3xl font-bold text-gray-800">Study Buddy</h1>
          </div>
          <p className="text-gray-600">Your AI learning companion using advanced prompt engineering</p>
        </div>

        {/* Chat Container */}
        <div className="bg-white rounded-lg shadow-lg overflow-hidden">
          {/* Messages */}
          <div className="h-96 overflow-y-auto p-4 space-y-4">
            {messages.map((message) => (
              <div
                key={message.id}
                className={`flex ${message.type === 'user' ? 'justify-end' : 'justify-start'}`}
              >
                <div
                  className={`max-w-xs lg:max-w-md px-4 py-2 rounded-lg ${
                    message.type === 'user'
                      ? 'bg-indigo-600 text-white'
                      : message.type === 'system'
                      ? 'bg-green-100 text-green-800 border border-green-200'
                      : 'bg-gray-100 text-gray-800'
                  }`}
                >
                  <div className="flex items-start gap-2">
                    {message.type === 'assistant' && (
                      <BookOpen className="w-4 h-4 mt-1 flex-shrink-0" />
                    )}
                    {message.type === 'system' && (
                      <MessageSquare className="w-4 h-4 mt-1 flex-shrink-0" />
                    )}
                    <p className="text-sm">{message.content}</p>
                  </div>
                </div>
              </div>
            ))}
            
            {isLoading && (
              <div className="flex justify-start">
                <div className="bg-gray-100 text-gray-800 max-w-xs lg:max-w-md px-4 py-2 rounded-lg">
                  <div className="flex items-center gap-2">
                    <BookOpen className="w-4 h-4" />
                    <div className="flex space-x-1">
                      <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></div>
                      <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{animationDelay: '0.1s'}}></div>
                      <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{animationDelay: '0.2s'}}></div>
                    </div>
                  </div>
                </div>
              </div>
            )}
          </div>

          {/* Input Section */}
          <div className="border-t p-4">
            <div className="flex gap-2">
              <input
                type="text"
                value={inputText}
                onChange={(e) => setInputText(e.target.value)}
                onKeyPress={(e) => e.key === 'Enter' && handleSubmit(e)}
                placeholder="What would you like to learn about?"
                className="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                disabled={isLoading}
              />
              <button
                onClick={handleSubmit}
                disabled={isLoading || !inputText.trim()}
                className="px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
              >
                <Send className="w-4 h-4" />
                Send
              </button>
            </div>
          </div>
        </div>

        {/* Technique Preview Panel (for future features) */}
        <div className="mt-6 bg-white rounded-lg shadow-lg p-6">
          <h3 className="text-lg font-semibold text-gray-800 mb-4">Available Techniques (Coming Soon)</h3>
          <div className="grid md:grid-cols-3 gap-4">
            <div className="p-4 border border-gray-200 rounded-lg bg-gray-50">
              <h4 className="font-medium text-gray-700">Zero-Shot</h4>
              <p className="text-sm text-gray-600 mt-1">Direct learning without examples</p>
            </div>
            <div className="p-4 border border-gray-200 rounded-lg bg-gray-50">
              <h4 className="font-medium text-gray-700">Few-Shot</h4>
              <p className="text-sm text-gray-600 mt-1">Learning with examples</p>
            </div>
            <div className="p-4 border border-gray-200 rounded-lg bg-gray-50">
              <h4 className="font-medium text-gray-700">Chain of Thought</h4>
              <p className="text-sm text-gray-600 mt-1">Step-by-step reasoning</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default StudyBuddy