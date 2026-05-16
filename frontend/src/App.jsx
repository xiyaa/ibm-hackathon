/**
 * Main application component with modern, beautiful design
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
  Paper,
  Chip,
  Stack,
  Button,
  IconButton,
  Tooltip,
} from '@mui/material';
import {
  Code as CodeIcon,
  AutoAwesome as AIIcon,
  GitHub as GitHubIcon,
  Speed as SpeedIcon,
  Home as HomeIcon,
  Refresh as RefreshIcon,
} from '@mui/icons-material';
import { AppProvider, useApp } from './context/AppContext';
import RepositoryInput from './components/RepositoryInput';
import OnboardingGuide from './components/OnboardingGuide';
import ChatInterface from './components/ChatInterface';
import LoadingSpinner from './components/LoadingSpinner';

// Create beautiful Material-UI theme
const theme = createTheme({
  palette: {
    mode: 'light',
    primary: {
      main: '#667eea',
      light: '#8b9cff',
      dark: '#4c63d2',
    },
    secondary: {
      main: '#764ba2',
      light: '#9d6cc9',
      dark: '#5a3a7d',
    },
    background: {
      default: '#f8f9ff',
      paper: '#ffffff',
    },
    text: {
      primary: '#2d3748',
      secondary: '#718096',
    },
  },
  typography: {
    fontFamily: '"Inter", "Roboto", "Helvetica", "Arial", sans-serif',
    h1: {
      fontWeight: 800,
      letterSpacing: '-0.02em',
    },
    h3: {
      fontWeight: 700,
      letterSpacing: '-0.01em',
    },
    h6: {
      fontWeight: 600,
    },
  },
  shape: {
    borderRadius: 16,
  },
  components: {
    MuiButton: {
      styleOverrides: {
        root: {
          textTransform: 'none',
          fontWeight: 600,
          borderRadius: 12,
          padding: '10px 24px',
        },
      },
    },
    MuiPaper: {
      styleOverrides: {
        root: {
          backgroundImage: 'none',
        },
      },
    },
  },
});

const AppContent = () => {
  const { isAnalyzing, analysisError, sessionId, cancelAnalysis, clearAnalysis } = useApp();

  const handleNewAnalysis = () => {
    clearAnalysis();
  };

  return (
    <Box sx={{ 
      minHeight: '100vh',
      background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
      position: 'relative',
      overflow: 'hidden',
    }}>
      {/* Animated background elements */}
      <Box sx={{
        position: 'absolute',
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        opacity: 0.1,
        background: 'radial-gradient(circle at 20% 50%, rgba(255,255,255,0.3) 0%, transparent 50%), radial-gradient(circle at 80% 80%, rgba(255,255,255,0.3) 0%, transparent 50%)',
        pointerEvents: 'none',
      }} />

      {/* App Bar with glass effect */}
      <AppBar 
        position="static" 
        elevation={0}
        sx={{
          background: 'rgba(255, 255, 255, 0.1)',
          backdropFilter: 'blur(10px)',
          borderBottom: '1px solid rgba(255, 255, 255, 0.2)',
        }}
      >
        <Toolbar sx={{ py: 1 }}>
          <Box sx={{
            display: 'flex',
            alignItems: 'center',
            gap: 1,
            background: 'rgba(255, 255, 255, 0.2)',
            px: 2,
            py: 0.5,
            borderRadius: 3,
          }}>
            <CodeIcon sx={{ fontSize: 28 }} />
            <Typography variant="h6" component="div" sx={{ fontWeight: 700 }}>
              DevPilot
            </Typography>
          </Box>
          <Box sx={{ flexGrow: 1 }} />
          
          {/* New Analysis Button - only show when there's a session */}
          {sessionId && !isAnalyzing && (
            <Tooltip title="Go to Home">
              <Button
                variant="contained"
                startIcon={<RefreshIcon />}
                onClick={handleNewAnalysis}
                sx={{
                  mr: 2,
                  background: 'rgba(255, 255, 255, 0.25)',
                  color: 'white',
                  fontWeight: 600,
                  backdropFilter: 'blur(10px)',
                  border: '1px solid rgba(255, 255, 255, 0.3)',
                  '&:hover': {
                    background: 'rgba(255, 255, 255, 0.35)',
                    transform: 'translateY(-2px)',
                    boxShadow: '0 4px 20px rgba(0,0,0,0.2)',
                  },
                  transition: 'all 0.3s ease',
                }}
              >
                Home
              </Button>
            </Tooltip>
          )}
          
          <Chip
            icon={<AIIcon />}
            label="Powered by IBM watsonx.ai"
            sx={{
              background: 'rgba(255, 255, 255, 0.2)',
              color: 'white',
              fontWeight: 600,
              '& .MuiChip-icon': { color: 'white' },
            }}
          />
        </Toolbar>
      </AppBar>

      {/* Main Content */}
      <Container maxWidth="lg" sx={{ py: 6, position: 'relative', zIndex: 1 }}>
        {/* Hero Section */}
        {!sessionId && !isAnalyzing && (
          <Box sx={{ textAlign: 'center', mb: 6, animation: 'fadeIn 0.8s ease-out' }}>
            <Box sx={{ mb: 3 }}>
              <Typography 
                variant="h1" 
                component="h1" 
                sx={{ 
                  fontSize: { xs: '2.5rem', md: '4rem' },
                  color: 'white',
                  mb: 2,
                  textShadow: '0 2px 20px rgba(0,0,0,0.2)',
                }}
              >
                Intelligent Developer
                <br />
                <span className="gradient-text" style={{ 
                  background: 'linear-gradient(135deg, #fff 0%, #f0f0ff 100%)',
                  WebkitBackgroundClip: 'text',
                  WebkitTextFillColor: 'transparent',
                }}>
                  Onboarding
                </span>
              </Typography>
              <Typography 
                variant="h5" 
                sx={{ 
                  color: 'rgba(255, 255, 255, 0.9)',
                  mb: 4,
                  fontWeight: 400,
                  maxWidth: '700px',
                  mx: 'auto',
                }}
              >
                Analyze any GitHub repository and get AI-powered insights in minutes
              </Typography>
            </Box>

            {/* Feature Cards */}
            <Stack 
              direction={{ xs: 'column', md: 'row' }} 
              spacing={3} 
              sx={{ mb: 5, justifyContent: 'center' }}
            >
              {[
                { icon: <GitHubIcon />, title: 'GitHub Integration', desc: 'Clone any public repository' },
                { icon: <AIIcon />, title: 'AI Analysis', desc: 'Powered by Granite models' },
                { icon: <SpeedIcon />, title: 'Fast Results', desc: 'Get insights in 1-2 minutes' },
              ].map((feature, index) => (
                <Paper
                  key={index}
                  elevation={0}
                  className="glass hover-lift"
                  sx={{
                    p: 3,
                    textAlign: 'center',
                    minWidth: { xs: '100%', md: '200px' },
                    animation: `slideIn 0.6s ease-out ${index * 0.1}s both`,
                  }}
                >
                  <Box sx={{ 
                    color: 'primary.main', 
                    mb: 1,
                    '& svg': { fontSize: 40 },
                  }}>
                    {feature.icon}
                  </Box>
                  <Typography variant="h6" gutterBottom sx={{ fontWeight: 700 }}>
                    {feature.title}
                  </Typography>
                  <Typography variant="body2" color="text.secondary">
                    {feature.desc}
                  </Typography>
                </Paper>
              ))}
            </Stack>
          </Box>
        )}

        {/* Repository Input Card */}
        <Paper 
          elevation={0}
          className="glass"
          sx={{ 
            p: 4, 
            mb: 4,
            animation: 'fadeIn 0.6s ease-out',
          }}
        >
          <RepositoryInput />
        </Paper>

        {/* Analysis Error */}
        {analysisError && (
          <Alert 
            severity="error" 
            sx={{ 
              mb: 3,
              borderRadius: 3,
              animation: 'slideIn 0.4s ease-out',
            }}
          >
            {analysisError}
          </Alert>
        )}

        {/* Loading State */}
        {isAnalyzing && (
          <Paper 
            elevation={0}
            className="glass"
            sx={{ 
              p: 6, 
              textAlign: 'center',
              animation: 'fadeIn 0.4s ease-out',
            }}
          >
            <LoadingSpinner
              message="Analyzing repository... This may take 1-2 minutes."
              size={60}
              onCancel={cancelAnalysis}
            />
          </Paper>
        )}

        {/* Results Section */}
        {!isAnalyzing && sessionId && (
          <Box sx={{ animation: 'fadeIn 0.6s ease-out' }}>
            <OnboardingGuide />
            <Box sx={{ mt: 4 }}>
              <ChatInterface />
            </Box>
          </Box>
        )}

        {/* Footer */}
        {!sessionId && !isAnalyzing && (
          <Box sx={{ textAlign: 'center', mt: 8, py: 4 }}>
            <Typography 
              variant="body1" 
              sx={{ 
                color: 'rgba(255, 255, 255, 0.9)',
                mb: 2,
                fontWeight: 500,
              }}
            >
              🚀 Enter a GitHub repository URL above to get started
            </Typography>
            <Typography 
              variant="caption" 
              sx={{ 
                color: 'rgba(255, 255, 255, 0.7)',
                display: 'block',
              }}
            >
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
