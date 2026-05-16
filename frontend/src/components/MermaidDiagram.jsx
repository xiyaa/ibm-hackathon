/**
 * Mermaid diagram component for rendering architecture and flow diagrams
 */

import React, { useEffect, useRef } from 'react';
import { Box, Paper, Typography } from '@mui/material';
import mermaid from 'mermaid';

// Initialize mermaid with configuration
mermaid.initialize({
  startOnLoad: true,
  theme: 'default',
  securityLevel: 'loose',
  fontFamily: 'Inter, Roboto, sans-serif',
  themeVariables: {
    primaryColor: '#667eea',
    primaryTextColor: '#2d3748',
    primaryBorderColor: '#667eea',
    lineColor: '#667eea',
    secondaryColor: '#764ba2',
    tertiaryColor: '#f8f9ff',
  },
});

const MermaidDiagram = ({ chart, title }) => {
  const mermaidRef = useRef(null);
  const [error, setError] = React.useState(null);

  useEffect(() => {
    if (mermaidRef.current && chart) {
      try {
        // Clear previous content
        mermaidRef.current.innerHTML = chart;
        
        // Render the diagram
        mermaid.contentLoaded();
        setError(null);
      } catch (err) {
        console.error('Mermaid rendering error:', err);
        setError('Error rendering diagram');
      }
    }
  }, [chart]);

  if (!chart) {
    return null;
  }

  if (error) {
    return (
      <Paper 
        elevation={0}
        sx={{ 
          p: 3, 
          mb: 3,
          bgcolor: 'error.light',
          color: 'error.contrastText',
        }}
      >
        <Typography variant="body2">{error}</Typography>
      </Paper>
    );
  }

  return (
    <Paper 
      elevation={0}
      sx={{ 
        p: 3, 
        mb: 3,
        bgcolor: 'background.paper',
        border: '1px solid',
        borderColor: 'divider',
        borderRadius: 2,
      }}
    >
      {title && (
        <Typography 
          variant="h6" 
          sx={{ 
            mb: 2, 
            fontWeight: 600,
            color: 'primary.main',
          }}
        >
          {title}
        </Typography>
      )}
      <Box
        ref={mermaidRef}
        className="mermaid"
        sx={{
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          minHeight: '200px',
          '& svg': {
            maxWidth: '100%',
            height: 'auto',
          },
        }}
      />
    </Paper>
  );
};

export default MermaidDiagram;

// Made with Bob
