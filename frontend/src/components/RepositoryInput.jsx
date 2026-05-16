/**
 * Repository input component for entering GitHub URLs
 */

import React, { useState } from 'react';
import {
  Box,
  TextField,
  Button,
  Paper,
  Typography,
  FormControlLabel,
  Checkbox,
  Alert,
} from '@mui/material';
import { GitHub as GitHubIcon, Refresh as RefreshIcon } from '@mui/icons-material';
import { useApp } from '../context/AppContext';
import { analyzeRepository } from '../services/api';

const RepositoryInput = () => {
  const {
    setIsAnalyzing,
    setAnalysisError,
    setAnalysisResults,
    clearAnalysis,
  } = useApp();

  const [repoUrl, setRepoUrl] = useState('');
  const [branch, setBranch] = useState('main');
  const [forceRefresh, setForceRefresh] = useState(false);
  const [localError, setLocalError] = useState('');

  const validateGitHubUrl = (url) => {
    const githubPattern = /^https?:\/\/(www\.)?github\.com\/[\w-]+\/[\w.-]+\/?$/;
    return githubPattern.test(url);
  };

  const handleAnalyze = async () => {
    setLocalError('');
    setAnalysisError(null);

    // Validate URL
    if (!repoUrl.trim()) {
      setLocalError('Please enter a GitHub repository URL');
      return;
    }

    if (!validateGitHubUrl(repoUrl.trim())) {
      setLocalError('Please enter a valid GitHub repository URL (e.g., https://github.com/username/repo)');
      return;
    }

    // Clear previous analysis
    clearAnalysis();
    setIsAnalyzing(true);

    try {
      const result = await analyzeRepository(repoUrl.trim(), branch.trim() || 'main', forceRefresh);
      setAnalysisResults(result);
      console.log('Analysis complete:', result);
    } catch (error) {
      console.error('Analysis error:', error);
      setAnalysisError(error.message || 'Failed to analyze repository');
    } finally {
      setIsAnalyzing(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleAnalyze();
    }
  };

  return (
    <Paper elevation={3} sx={{ p: 3, mb: 3 }}>
      <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
        <GitHubIcon sx={{ mr: 1, fontSize: 32 }} />
        <Typography variant="h5" component="h2">
          Analyze GitHub Repository
        </Typography>
      </Box>

      <Typography variant="body2" color="text.secondary" sx={{ mb: 3 }}>
        Enter a GitHub repository URL to generate an AI-powered onboarding guide
      </Typography>

      {localError && (
        <Alert severity="error" sx={{ mb: 2 }} onClose={() => setLocalError('')}>
          {localError}
        </Alert>
      )}

      <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
        <TextField
          fullWidth
          label="GitHub Repository URL"
          placeholder="https://github.com/username/repository"
          value={repoUrl}
          onChange={(e) => setRepoUrl(e.target.value)}
          onKeyPress={handleKeyPress}
          variant="outlined"
          helperText="Example: https://github.com/fastapi/fastapi"
        />

        <Box sx={{ display: 'flex', gap: 2, alignItems: 'center' }}>
          <TextField
            label="Branch"
            placeholder="main"
            value={branch}
            onChange={(e) => setBranch(e.target.value)}
            onKeyPress={handleKeyPress}
            variant="outlined"
            sx={{ flex: 1 }}
            helperText="Leave empty for default branch"
          />

          <FormControlLabel
            control={
              <Checkbox
                checked={forceRefresh}
                onChange={(e) => setForceRefresh(e.target.checked)}
              />
            }
            label="Force refresh"
          />
        </Box>

        <Button
          variant="contained"
          size="large"
          onClick={handleAnalyze}
          startIcon={<RefreshIcon />}
          sx={{ alignSelf: 'flex-start' }}
        >
          Analyze Repository
        </Button>
      </Box>

      <Box sx={{ mt: 3, p: 2, bgcolor: 'grey.100', borderRadius: 1 }}>
        <Typography variant="caption" color="text.secondary">
          <strong>Note:</strong> Analysis may take 1-5 minutes depending on repository size.
          The AI will analyze the code structure, dependencies, and generate a comprehensive onboarding guide.
        </Typography>
      </Box>
    </Paper>
  );
};

export default RepositoryInput;

// Made with Bob
