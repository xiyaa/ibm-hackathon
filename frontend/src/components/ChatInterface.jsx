/**
 * Chat interface component for interacting with the AI
 */

import React, { useState, useRef, useEffect } from 'react';
import {
  Box,
  Paper,
  TextField,
  Button,
  Typography,
  Avatar,
  IconButton,
  Alert,
} from '@mui/material';
import {
  Send as SendIcon,
  Person as PersonIcon,
  SmartToy as BotIcon,
  Clear as ClearIcon,
} from '@mui/icons-material';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { vscDarkPlus } from 'react-syntax-highlighter/dist/esm/styles/prism';
import { useApp } from '../context/AppContext';
import { sendChatMessage } from '../services/api';
import CodeReference from './CodeReference';

const ChatInterface = () => {
  const {
    sessionId,
    messages,
    isChatting,
    chatError,
    setIsChatting,
    setChatError,
    addMessage,
    clearMessages,
  } = useApp();

  const [inputMessage, setInputMessage] = useState('');
  const messagesEndRef = useRef(null);
  const inputRef = useRef(null);

  // Auto-scroll to bottom when new messages arrive
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  // Focus input on mount
  useEffect(() => {
    if (sessionId) {
      inputRef.current?.focus();
    }
  }, [sessionId]);

  const handleSendMessage = async () => {
    if (!inputMessage.trim() || !sessionId || isChatting) {
      return;
    }

    const userMessage = inputMessage.trim();
    setInputMessage('');
    setChatError(null);

    // Add user message to chat
    addMessage({
      role: 'user',
      content: userMessage,
      timestamp: new Date().toISOString(),
    });

    setIsChatting(true);

    try {
      const response = await sendChatMessage(sessionId, userMessage);
      
      // Add assistant message to chat
      addMessage({
        role: 'assistant',
        content: response.response,
        references: response.references || [],
        timestamp: response.timestamp,
      });
    } catch (error) {
      console.error('Chat error:', error);
      setChatError(error.message || 'Failed to send message');
    } finally {
      setIsChatting(false);
      inputRef.current?.focus();
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  const handleClearChat = () => {
    clearMessages();
  };

  if (!sessionId) {
    return null;
  }

  return (
    <Paper elevation={3} sx={{ p: 3, display: 'flex', flexDirection: 'column', height: '600px' }}>
      {/* Header */}
      <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', mb: 2 }}>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
          <BotIcon color="primary" />
          <Typography variant="h6">Chat with AI</Typography>
        </Box>
        {messages.length > 0 && (
          <IconButton size="small" onClick={handleClearChat} title="Clear chat">
            <ClearIcon />
          </IconButton>
        )}
      </Box>

      {chatError && (
        <Alert severity="error" sx={{ mb: 2 }} onClose={() => setChatError(null)}>
          {chatError}
        </Alert>
      )}

      {/* Messages Container */}
      <Box
        sx={{
          flex: 1,
          overflowY: 'auto',
          mb: 2,
          p: 2,
          bgcolor: 'grey.50',
          borderRadius: 1,
          display: 'flex',
          flexDirection: 'column',
          gap: 2,
        }}
      >
        {messages.length === 0 ? (
          <Box sx={{ textAlign: 'center', py: 4 }}>
            <BotIcon sx={{ fontSize: 48, color: 'grey.400', mb: 2 }} />
            <Typography variant="body1" color="text.secondary">
              Ask me anything about this codebase!
            </Typography>
            <Typography variant="body2" color="text.secondary" sx={{ mt: 1 }}>
              Examples: "How does authentication work?", "What's the project structure?", "Explain the main components"
            </Typography>
          </Box>
        ) : (
          messages.map((message, index) => (
            <Box
              key={index}
              sx={{
                display: 'flex',
                gap: 2,
                alignItems: 'flex-start',
              }}
            >
              <Avatar
                sx={{
                  bgcolor: message.role === 'user' ? 'primary.main' : 'secondary.main',
                  width: 32,
                  height: 32,
                }}
              >
                {message.role === 'user' ? <PersonIcon fontSize="small" /> : <BotIcon fontSize="small" />}
              </Avatar>
              <Box sx={{ flex: 1 }}>
                <Typography variant="caption" color="text.secondary" sx={{ mb: 0.5, display: 'block' }}>
                  {message.role === 'user' ? 'You' : 'AI Assistant'}
                </Typography>
                <Paper
                  elevation={1}
                  sx={{
                    p: 2,
                    bgcolor: message.role === 'user' ? 'primary.50' : 'white',
                  }}
                >
                  {message.role === 'user' ? (
                    <Typography variant="body1">{message.content}</Typography>
                  ) : (
                    <>
                      <ReactMarkdown
                        remarkPlugins={[remarkGfm]}
                        components={{
                          code({ node, inline, className, children, ...props }) {
                            const match = /language-(\w+)/.exec(className || '');
                            return !inline && match ? (
                              <SyntaxHighlighter
                                style={vscDarkPlus}
                                language={match[1]}
                                PreTag="div"
                                customStyle={{ fontSize: '0.875rem' }}
                                {...props}
                              >
                                {String(children).replace(/\n$/, '')}
                              </SyntaxHighlighter>
                            ) : (
                              <code className={className} {...props}>
                                {children}
                              </code>
                            );
                          },
                        }}
                      >
                        {message.content}
                      </ReactMarkdown>
                      {message.references && message.references.length > 0 && (
                        <Box sx={{ mt: 2 }}>
                          <Typography variant="caption" color="text.secondary" sx={{ mb: 1, display: 'block' }}>
                            Code References:
                          </Typography>
                          {message.references.map((ref, refIndex) => (
                            <CodeReference
                              key={refIndex}
                              file={ref.file}
                              lines={ref.lines}
                              snippet={ref.snippet}
                              language={ref.language}
                            />
                          ))}
                        </Box>
                      )}
                    </>
                  )}
                </Paper>
              </Box>
            </Box>
          ))
        )}
        {isChatting && (
          <Box sx={{ display: 'flex', gap: 2, alignItems: 'flex-start' }}>
            <Avatar sx={{ bgcolor: 'secondary.main', width: 32, height: 32 }}>
              <BotIcon fontSize="small" />
            </Avatar>
            <Paper elevation={1} sx={{ p: 2, bgcolor: 'white' }}>
              <Typography variant="body2" color="text.secondary">
                Thinking...
              </Typography>
            </Paper>
          </Box>
        )}
        <div ref={messagesEndRef} />
      </Box>

      {/* Input Area */}
      <Box sx={{ display: 'flex', gap: 1 }}>
        <TextField
          fullWidth
          multiline
          maxRows={4}
          placeholder="Ask a question about the codebase..."
          value={inputMessage}
          onChange={(e) => setInputMessage(e.target.value)}
          onKeyPress={handleKeyPress}
          disabled={isChatting}
          inputRef={inputRef}
          variant="outlined"
        />
        <Button
          variant="contained"
          onClick={handleSendMessage}
          disabled={!inputMessage.trim() || isChatting}
          endIcon={<SendIcon />}
          sx={{ minWidth: '100px' }}
        >
          Send
        </Button>
      </Box>
    </Paper>
  );
};

export default ChatInterface;

// Made with Bob
