/**
 * Mermaid diagram component for rendering architecture and flow diagrams
 */

import React, { useEffect, useRef, useState } from 'react';
import { Box, Paper, Typography, CircularProgress } from '@mui/material';
import mermaid from 'mermaid';

// Initialize mermaid with enhanced configuration
mermaid.initialize({
  startOnLoad: false,
  theme: 'default',
  securityLevel: 'loose',
  fontFamily: 'Inter, Roboto, sans-serif',
  fontSize: 14,
  themeVariables: {
    primaryColor: '#667eea',
    primaryTextColor: '#2d3748',
    primaryBorderColor: '#667eea',
    lineColor: '#667eea',
    secondaryColor: '#764ba2',
    tertiaryColor: '#f8f9ff',
    background: '#ffffff',
    mainBkg: '#e3f2fd',
    secondBkg: '#fff3e0',
    tertiaryBkg: '#f3e5f5',
    nodeBorder: '#667eea',
    clusterBkg: '#f8f9ff',
    clusterBorder: '#667eea',
    titleColor: '#2d3748',
    edgeLabelBackground: '#ffffff',
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
      elevation={2}
      sx={{
        p: 3,
        mb: 3,
        bgcolor: 'background.paper',
        border: '2px solid',
        borderColor: 'primary.light',
        borderRadius: 3,
        overflow: 'hidden',
        transition: 'all 0.3s ease',
        '&:hover': {
          boxShadow: 6,
          transform: 'translateY(-2px)',
        },
      }}
    >
      {title && (
        <Box
          sx={{
            mb: 3,
            pb: 2,
            borderBottom: '2px solid',
            borderColor: 'divider',
          }}
        >
          <Typography
            variant="h6"
            sx={{
              fontWeight: 700,
              color: 'primary.main',
              display: 'flex',
              alignItems: 'center',
              gap: 1,
            }}
          >
            {title}
          </Typography>
        </Box>
      )}
      {loading ? (
        <Box sx={{ display: 'flex', justifyContent: 'center', p: 6 }}>
          <CircularProgress size={48} />
        </Box>
      ) : (
        <Box
          ref={mermaidRef}
          sx={{
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            minHeight: '300px',
            bgcolor: '#fafafa',
            borderRadius: 2,
            p: 2,
            overflow: 'auto',
            '& svg': {
              maxWidth: '100%',
              height: 'auto',
              minHeight: '250px',
            },
            '& .node rect, & .node circle, & .node ellipse, & .node polygon': {
              transition: 'all 0.2s ease',
            },
            '& .node:hover rect, & .node:hover circle, & .node:hover ellipse, & .node:hover polygon': {
              filter: 'brightness(0.95)',
              strokeWidth: '2px',
            },
          }}
          dangerouslySetInnerHTML={{ __html: svg }}
        />
      )}
    </Paper>
  );
};

export default MermaidDiagram;
