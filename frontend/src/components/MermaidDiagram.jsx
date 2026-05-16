/**
 * Mermaid diagram component for rendering architecture and flow diagrams
 */

import React, { useEffect, useRef, useState } from 'react';
import { Box, Paper, Typography, CircularProgress } from '@mui/material';
import mermaid from 'mermaid';

// Initialize mermaid with configuration
mermaid.initialize({
  startOnLoad: false,
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
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);
  const [svg, setSvg] = useState('');

  useEffect(() => {
    const renderDiagram = async () => {
      if (!chart) {
        setLoading(false);
        return;
      }

      try {
        setLoading(true);
        setError(null);
        
        // Generate unique ID for this diagram
        const id = `mermaid-${Math.random().toString(36).substr(2, 9)}`;
        
        // Render the diagram
        const { svg: renderedSvg } = await mermaid.render(id, chart);
        setSvg(renderedSvg);
        setLoading(false);
      } catch (err) {
        console.error('Mermaid rendering error:', err);
        setError(`Error rendering diagram: ${err.message}`);
        setLoading(false);
      }
    };

    renderDiagram();
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
      {loading ? (
        <Box sx={{ display: 'flex', justifyContent: 'center', p: 4 }}>
          <CircularProgress />
        </Box>
      ) : (
        <Box
          ref={mermaidRef}
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
          dangerouslySetInnerHTML={{ __html: svg }}
        />
      )}
    </Paper>
  );
};

export default MermaidDiagram;
