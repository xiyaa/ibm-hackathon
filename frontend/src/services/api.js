/**
 * API client for DevOnboard AI backend
 */

import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

// Create axios instance with default config
const apiClient = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 120000, // 2 minutes for analysis operations
});

// Request interceptor
apiClient.interceptors.request.use(
  (config) => {
    console.log(`API Request: ${config.method.toUpperCase()} ${config.url}`);
    return config;
  },
  (error) => {
    console.error('API Request Error:', error);
    return Promise.reject(error);
  }
);

// Response interceptor
apiClient.interceptors.response.use(
  (response) => {
    console.log(`API Response: ${response.status} ${response.config.url}`);
    return response;
  },
  (error) => {
    console.error('API Response Error:', error.response?.data || error.message);
    return Promise.reject(error);
  }
);

/**
 * Analyze a GitHub repository
 * @param {string} repoUrl - GitHub repository URL
 * @param {string} branch - Branch name (default: 'main')
 * @param {boolean} forceRefresh - Force re-analysis
 * @returns {Promise} Analysis results
 */
export const analyzeRepository = async (repoUrl, branch = 'main', forceRefresh = false) => {
  try {
    const response = await apiClient.post('/api/analyze', {
      repo_url: repoUrl,
      branch,
      force_refresh: forceRefresh,
    });
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.detail || 'Failed to analyze repository');
  }
};

/**
 * Send a chat message
 * @param {string} sessionId - Session ID from analysis
 * @param {string} message - User message
 * @param {object} context - Optional file context
 * @returns {Promise} Chat response
 */
export const sendChatMessage = async (sessionId, message, context = null) => {
  try {
    const response = await apiClient.post('/api/chat', {
      session_id: sessionId,
      message,
      context,
    });
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.detail || 'Failed to send message');
  }
};

/**
 * Get chat history for a session
 * @param {string} sessionId - Session ID
 * @returns {Promise} Chat history
 */
export const getChatHistory = async (sessionId) => {
  try {
    const response = await apiClient.get(`/api/chat/history/${sessionId}`);
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.detail || 'Failed to get chat history');
  }
};

/**
 * Get file tree for a session
 * @param {string} sessionId - Session ID
 * @returns {Promise} File tree
 */
export const getFileTree = async (sessionId) => {
  try {
    const response = await apiClient.get(`/api/files/${sessionId}`);
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.detail || 'Failed to get file tree');
  }
};

/**
 * Get file content
 * @param {string} sessionId - Session ID
 * @param {string} filePath - File path
 * @returns {Promise} File content
 */
export const getFileContent = async (sessionId, filePath) => {
  try {
    const response = await apiClient.get(`/api/files/${sessionId}/content`, {
      params: { path: filePath },
    });
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.detail || 'Failed to get file content');
  }
};

/**
 * Health check
 * @returns {Promise} Health status
 */
export const healthCheck = async () => {
  try {
    const response = await apiClient.get('/health');
    return response.data;
  } catch (error) {
    throw new Error('Backend is not available');
  }
};

export default apiClient;

// Made with Bob
