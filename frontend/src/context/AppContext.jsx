/**
 * Global application context for state management
 */

import React, { createContext, useContext, useState, useCallback } from 'react';

const AppContext = createContext(null);

export const AppProvider = ({ children }) => {
  // Analysis state
  const [sessionId, setSessionId] = useState(null);
  const [repository, setRepository] = useState(null);
  const [analysis, setAnalysis] = useState(null);
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [analysisError, setAnalysisError] = useState(null);

  // Chat state
  const [messages, setMessages] = useState([]);
  const [isChatting, setIsChatting] = useState(false);
  const [chatError, setChatError] = useState(null);

  // File context state
  const [selectedFile, setSelectedFile] = useState(null);
  const [fileContent, setFileContent] = useState(null);

  /**
   * Set analysis results
   */
  const setAnalysisResults = useCallback((data) => {
    setSessionId(data.session_id);
    setRepository(data.repository);
    setAnalysis(data.analysis);
    setAnalysisError(null);
  }, []);

  /**
   * Clear analysis results
   */
  const clearAnalysis = useCallback(() => {
    setSessionId(null);
    setRepository(null);
    setAnalysis(null);
    setMessages([]);
    setSelectedFile(null);
    setFileContent(null);
    setAnalysisError(null);
    setChatError(null);
  }, []);

  /**
   * Cancel ongoing analysis
   */
  const cancelAnalysis = useCallback(() => {
    setIsAnalyzing(false);
    setAnalysisError('Analysis cancelled by user');
  }, []);

  /**
   * Add a chat message
   */
  const addMessage = useCallback((message) => {
    setMessages((prev) => [...prev, message]);
  }, []);

  /**
   * Add multiple messages
   */
  const addMessages = useCallback((newMessages) => {
    setMessages((prev) => [...prev, ...newMessages]);
  }, []);

  /**
   * Clear chat messages
   */
  const clearMessages = useCallback(() => {
    setMessages([]);
    setChatError(null);
  }, []);

  /**
   * Set selected file for context
   */
  const selectFile = useCallback((file, content = null) => {
    setSelectedFile(file);
    setFileContent(content);
  }, []);

  /**
   * Clear selected file
   */
  const clearSelectedFile = useCallback(() => {
    setSelectedFile(null);
    setFileContent(null);
  }, []);

  const value = {
    // Analysis state
    sessionId,
    repository,
    analysis,
    isAnalyzing,
    analysisError,
    setIsAnalyzing,
    setAnalysisError,
    setAnalysisResults,
    clearAnalysis,
    cancelAnalysis,

    // Chat state
    messages,
    isChatting,
    chatError,
    setIsChatting,
    setChatError,
    addMessage,
    addMessages,
    clearMessages,

    // File context state
    selectedFile,
    fileContent,
    selectFile,
    clearSelectedFile,
  };

  return <AppContext.Provider value={value}>{children}</AppContext.Provider>;
};

/**
 * Hook to use app context
 */
export const useApp = () => {
  const context = useContext(AppContext);
  if (!context) {
    throw new Error('useApp must be used within AppProvider');
  }
  return context;
};

export default AppContext;

// Made with Bob
