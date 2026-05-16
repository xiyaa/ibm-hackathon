/**
 * Main application component
 */

import React from 'react';
import {
  Container,
  Box,
  Typography,
  AppBar,
  Toolbar,
  Alert,
  CssBaseline,
  ThemeProvider,
  createTheme,
} from '@mui/material';
import { Code as CodeIcon } from '@mui/icons-material';
import { AppProvider, useApp } from './context/AppContext';
import RepositoryInput from './components/RepositoryInput';
import OnboardingGuide from './components/OnboardingGuide';
import ChatInterface from './components/ChatInterface';
import LoadingSpinner from './components/LoadingSpinner';

// Create Material-UI theme
const theme = createTheme({
  palette: {
    primary: {
      main: '#0f62fe',
    },
    secondary: {
      main: '#8a3ffc',
    },
  },
  typography: {
    fontFamily: '"Inter", "Roboto", "Helvetica", "Arial", sans-serif',
  },
});

const AppContent = () => {
  const { isAnalyzing, analysisError, sessionId } = useApp();

  return (
    <Box sx={{ minHeight: '100vh', bgcolor: 'grey.100' }}>
      {/* App Bar */}
      <AppBar position="static" elevation={2}>
        <Toolbar>
          <CodeIcon sx={{ mr: 2 }} />
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            DevOnboard AI
          </Typography>
          <Typography variant="body2" sx={{ opacity: 0.8 }}>
            Powered by IBM watsonx.ai
          </Typography>
        </Toolbar>
      </AppBar>

      {/* Main Content */}
      <Container maxWidth="lg" sx={{ py: 4 }}>
        {/* Hero Section */}
        <Box sx={{ textAlign: 'center', mb: 4 }}>
          <Typography variant="h3" component="h1" gutterBottom>
            Intelligent Developer Onboarding
          </Typography>
          <Typography variant="h6" color="text.secondary" sx={{ mb: 2 }}>
            Analyze any GitHub repository and get AI-powered insights in minutes
          </Typography>
        </Box>

        {/* Repository Input */}
        <RepositoryInput />

        {/* Analysis Error */}
        {analysisError && (
          <Alert severity="error" sx={{ mb: 3 }}>
            {analysisError}
          </Alert>
        )}

        {/* Loading State */}
        {isAnalyzing && (
          <Box sx={{ my: 4 }}>
            <LoadingSpinner
              message="Analyzing repository... This may take 1-2 minutes."
              size={60}
            />
          </Box>
        )}

        {/* Onboarding Guide */}
        {!isAnalyzing && sessionId && (
          <>
            <OnboardingGuide />
            <ChatInterface />
          </>
        )}

        {/* Footer */}
        {!sessionId && !isAnalyzing && (
          <Box sx={{ textAlign: 'center', mt: 6, py: 4 }}>
            <Typography variant="body2" color="text.secondary">
              Enter a GitHub repository URL above to get started
            </Typography>
            <Typography variant="caption" color="text.secondary" sx={{ mt: 1, display: 'block' }}>
              Built for IBM Hackathon • Powered by watsonx.ai Granite Models
            </Typography>
          </Box>
        )}
      </Container>
    </Box>
  );
};

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <AppProvider>
        <AppContent />
      </AppProvider>
    </ThemeProvider>
  );
}

export default App;

// Made with Bob
