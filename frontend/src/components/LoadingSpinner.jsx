/**
 * Loading spinner component with cancel button
 */

import React from 'react';
import { Box, CircularProgress, Typography, Button } from '@mui/material';
import { Cancel as CancelIcon } from '@mui/icons-material';

const LoadingSpinner = ({ message = 'Loading...', size = 40, onCancel }) => {
  return (
    <Box
      sx={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        padding: 4,
        gap: 2,
      }}
    >
      <CircularProgress size={size} thickness={4} />
      {message && (
        <Typography variant="body1" color="text.secondary" sx={{ textAlign: 'center' }}>
          {message}
        </Typography>
      )}
      {onCancel && (
        <Button
          variant="outlined"
          color="error"
          startIcon={<CancelIcon />}
          onClick={onCancel}
          sx={{
            mt: 2,
            borderRadius: 3,
            textTransform: 'none',
            fontWeight: 600,
            '&:hover': {
              transform: 'translateY(-2px)',
              boxShadow: 2,
            },
            transition: 'all 0.2s',
          }}
        >
          Cancel Analysis
        </Button>
      )}
    </Box>
  );
};

export default LoadingSpinner;

// Made with Bob
