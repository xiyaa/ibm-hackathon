/**
 * Code reference component for displaying code snippets
 */

import React from 'react';
import { Box, Paper, Typography, Chip } from '@mui/material';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { vscDarkPlus } from 'react-syntax-highlighter/dist/esm/styles/prism';
import { Code as CodeIcon } from '@mui/icons-material';

const CodeReference = ({ file, lines, snippet, language }) => {
  return (
    <Paper
      elevation={2}
      sx={{
        p: 2,
        mb: 2,
        bgcolor: 'grey.50',
        border: '1px solid',
        borderColor: 'grey.300',
      }}
    >
      <Box sx={{ display: 'flex', alignItems: 'center', mb: 1, gap: 1 }}>
        <CodeIcon fontSize="small" color="primary" />
        <Typography variant="subtitle2" sx={{ fontFamily: 'monospace', flex: 1 }}>
          {file}
        </Typography>
        {lines && lines.length > 0 && (
          <Chip
            label={`Lines ${lines[0]}-${lines[lines.length - 1]}`}
            size="small"
            variant="outlined"
          />
        )}
        {language && (
          <Chip label={language} size="small" color="primary" variant="outlined" />
        )}
      </Box>

      {snippet && (
        <Box sx={{ mt: 1 }}>
          <SyntaxHighlighter
            language={language || 'text'}
            style={vscDarkPlus}
            customStyle={{
              margin: 0,
              borderRadius: '4px',
              fontSize: '0.875rem',
            }}
            showLineNumbers
            startingLineNumber={lines && lines.length > 0 ? lines[0] : 1}
          >
            {snippet}
          </SyntaxHighlighter>
        </Box>
      )}
    </Paper>
  );
};

export default CodeReference;

// Made with Bob
