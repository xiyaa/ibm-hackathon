/**
 * Beautiful onboarding guide component with enhanced markdown styling
 */

import React, { useState } from 'react';
import {
  Box,
  Paper,
  Typography,
  Chip,
  Divider,
  Accordion,
  AccordionSummary,
  AccordionDetails,
  Alert,
  Card,
  CardContent,
  Grid,
  Stack,
  IconButton,
  Tooltip,
} from '@mui/material';
import {
  ExpandMore as ExpandMoreIcon,
  CheckCircle as CheckCircleIcon,
  Info as InfoIcon,
  Code as CodeIcon,
  Architecture as ArchitectureIcon,
  Description as FileIcon,
  Extension as DependencyIcon,
  PlayArrow as SetupIcon,
  ContentCopy as CopyIcon,
  AccountTree as DiagramIcon,
} from '@mui/icons-material';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { vscDarkPlus } from 'react-syntax-highlighter/dist/esm/styles/prism';
import { useApp } from '../context/AppContext';
import MermaidDiagram from './MermaidDiagram';

// Custom markdown components with beautiful styling
const MarkdownComponents = {
  h1: ({ children }) => (
    <Typography 
      variant="h4" 
      sx={{ 
        mt: 3, 
        mb: 2, 
        fontWeight: 700,
        background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        WebkitBackgroundClip: 'text',
        WebkitTextFillColor: 'transparent',
      }}
    >
      {children}
    </Typography>
  ),
  h2: ({ children }) => (
    <Typography 
      variant="h5" 
      sx={{ 
        mt: 3, 
        mb: 2, 
        fontWeight: 600,
        color: 'primary.main',
        display: 'flex',
        alignItems: 'center',
        gap: 1,
      }}
    >
      <Box sx={{ 
        width: 4, 
        height: 24, 
        bgcolor: 'primary.main',
        borderRadius: 1,
      }} />
      {children}
    </Typography>
  ),
  h3: ({ children }) => (
    <Typography 
      variant="h6" 
      sx={{ 
        mt: 2, 
        mb: 1.5, 
        fontWeight: 600,
        color: 'text.primary',
      }}
    >
      {children}
    </Typography>
  ),
  p: ({ children }) => (
    <Typography 
      variant="body1" 
      sx={{ 
        mb: 2, 
        lineHeight: 1.8,
        color: 'text.secondary',
      }}
    >
      {children}
    </Typography>
  ),
  ul: ({ children }) => (
    <Box 
      component="ul" 
      sx={{ 
        pl: 3, 
        mb: 2,
        '& li': {
          mb: 1,
          lineHeight: 1.8,
          color: 'text.secondary',
        },
        '& li::marker': {
          color: 'primary.main',
          fontSize: '1.2em',
        },
      }}
    >
      {children}
    </Box>
  ),
  ol: ({ children }) => (
    <Box 
      component="ol" 
      sx={{ 
        pl: 3, 
        mb: 2,
        '& li': {
          mb: 1,
          lineHeight: 1.8,
          color: 'text.secondary',
        },
        '& li::marker': {
          color: 'primary.main',
          fontWeight: 600,
        },
      }}
    >
      {children}
    </Box>
  ),
  blockquote: ({ children }) => (
    <Paper
      sx={{
        borderLeft: 4,
        borderColor: 'primary.main',
        bgcolor: 'primary.50',
        p: 2,
        mb: 2,
        fontStyle: 'italic',
      }}
    >
      {children}
    </Paper>
  ),
  code({ node, inline, className, children, ...props }) {
    const match = /language-(\w+)/.exec(className || '');
    const [copied, setCopied] = useState(false);
    
    const handleCopy = () => {
      navigator.clipboard.writeText(String(children));
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    };

    return !inline && match ? (
      <Box sx={{ position: 'relative', mb: 2 }}>
        <Tooltip title={copied ? "Copied!" : "Copy code"}>
          <IconButton
            size="small"
            onClick={handleCopy}
            sx={{
              position: 'absolute',
              right: 8,
              top: 8,
              zIndex: 1,
              bgcolor: 'rgba(255,255,255,0.1)',
              '&:hover': { bgcolor: 'rgba(255,255,255,0.2)' },
            }}
          >
            <CopyIcon fontSize="small" sx={{ color: 'white' }} />
          </IconButton>
        </Tooltip>
        <SyntaxHighlighter
          style={vscDarkPlus}
          language={match[1]}
          PreTag="div"
          customStyle={{
            borderRadius: 12,
            padding: '20px',
            fontSize: '0.9rem',
          }}
          {...props}
        >
          {String(children).replace(/\n$/, '')}
        </SyntaxHighlighter>
      </Box>
    ) : (
      <Box
        component="code"
        sx={{
          bgcolor: 'grey.100',
          color: 'error.main',
          px: 1,
          py: 0.5,
          borderRadius: 1,
          fontFamily: 'monospace',
          fontSize: '0.9em',
        }}
        {...props}
      >
        {children}
      </Box>
    );
  },
  table: ({ children }) => (
    <Box sx={{ overflowX: 'auto', mb: 2 }}>
      <Box
        component="table"
        sx={{
          width: '100%',
          borderCollapse: 'collapse',
          '& th': {
            bgcolor: 'primary.main',
            color: 'white',
            p: 1.5,
            textAlign: 'left',
            fontWeight: 600,
          },
          '& td': {
            p: 1.5,
            borderBottom: '1px solid',
            borderColor: 'divider',
          },
          '& tr:hover': {
            bgcolor: 'action.hover',
          },
        }}
      >
        {children}
      </Box>
    </Box>
  ),
};

const OnboardingGuide = () => {
  const { repository, analysis } = useApp();

  if (!repository || !analysis) {
    return null;
  }

  return (
    <Paper 
      elevation={0}
      className="glass"
      sx={{ 
        p: 4,
        mb: 3,
        animation: 'fadeIn 0.6s ease-out',
      }}
    >
      {/* Repository Header with gradient */}
      <Box sx={{ mb: 4 }}>
        <Box sx={{ 
          display: 'flex', 
          alignItems: 'center', 
          gap: 2, 
          mb: 2,
          pb: 2,
          borderBottom: '2px solid',
          borderImage: 'linear-gradient(90deg, #667eea 0%, #764ba2 100%) 1',
        }}>
          <CheckCircleIcon sx={{ fontSize: 40, color: 'success.main' }} />
          <Box>
            <Typography 
              variant="h4" 
              component="h2"
              sx={{ 
                fontWeight: 700,
                background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
                WebkitBackgroundClip: 'text',
                WebkitTextFillColor: 'transparent',
              }}
            >
              {repository.name}
            </Typography>
            <Typography variant="body2" color="text.secondary">
              {repository.owner} • {repository.branch} • {repository.last_commit?.substring(0, 7)}
            </Typography>
          </Box>
        </Box>

        {/* Tech Stack with beautiful chips */}
        {analysis.tech_stack && analysis.tech_stack.length > 0 && (
          <Stack direction="row" spacing={1} flexWrap="wrap" useFlexGap>
            {analysis.tech_stack.map((tech, index) => (
              <Chip 
                key={index} 
                label={tech} 
                sx={{
                  background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
                  color: 'white',
                  fontWeight: 600,
                  '&:hover': {
                    transform: 'translateY(-2px)',
                    boxShadow: 2,
                  },
                  transition: 'all 0.2s',
                }}
              />
            ))}
          </Stack>
        )}
      </Box>

      {/* Overview Section with icon - ALWAYS VISIBLE */}
      {analysis.overview && (
        <Card
          elevation={0}
          sx={{
            mb: 3,
            border: '2px solid',
            borderColor: 'primary.light',
            borderRadius: 3,
            overflow: 'hidden',
          }}
        >
          <Box sx={{
            bgcolor: 'primary.main',
            color: 'white',
            p: 2,
            display: 'flex',
            alignItems: 'center',
            gap: 1,
          }}>
            <InfoIcon />
            <Typography variant="h6" sx={{ fontWeight: 600 }}>
              📋 Project Overview
            </Typography>
          </Box>
          <CardContent sx={{ p: 3 }}>
            <ReactMarkdown
              remarkPlugins={[remarkGfm]}
              components={MarkdownComponents}
            >
              {analysis.overview}
            </ReactMarkdown>
          </CardContent>
        </Card>
      )}

      {/* Architecture Insights - EXPANDED BY DEFAULT */}
      {analysis.architecture_insights && (
        <Accordion
          defaultExpanded
          sx={{
            mb: 2,
            borderRadius: '12px !important',
            '&:before': { display: 'none' },
            boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
          }}
        >
          <AccordionSummary
            expandIcon={<ExpandMoreIcon />}
            sx={{
              bgcolor: 'secondary.light',
              color: 'secondary.dark',
              borderRadius: '12px 12px 0 0',
              '&:hover': { bgcolor: 'secondary.main', color: 'white' },
            }}
          >
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
              <ArchitectureIcon />
              <Typography variant="h6" sx={{ fontWeight: 600 }}>
                🏗️ Architecture Insights
              </Typography>
            </Box>
          </AccordionSummary>
          <AccordionDetails sx={{ p: 3 }}>
            <ReactMarkdown
              remarkPlugins={[remarkGfm]}
              components={MarkdownComponents}
            >
              {analysis.architecture_insights}
            </ReactMarkdown>
          </AccordionDetails>
        </Accordion>
      )}

      {/* Setup Instructions - EXPANDED BY DEFAULT */}
      {analysis.setup_instructions && (
        <Accordion
          defaultExpanded
          sx={{
            mb: 2,
            borderRadius: '12px !important',
            '&:before': { display: 'none' },
            boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
          }}
        >
          <AccordionSummary
            expandIcon={<ExpandMoreIcon />}
            sx={{
              bgcolor: 'success.light',
              color: 'success.dark',
              borderRadius: '12px 12px 0 0',
              '&:hover': { bgcolor: 'success.main', color: 'white' },
            }}
          >
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
              <SetupIcon />
              <Typography variant="h6" sx={{ fontWeight: 600 }}>
                🚀 Setup Instructions
              </Typography>
            </Box>
          </AccordionSummary>
          <AccordionDetails sx={{ p: 3 }}>
            <ReactMarkdown
              remarkPlugins={[remarkGfm]}
              components={MarkdownComponents}
            >
              {analysis.setup_instructions}
            </ReactMarkdown>
          </AccordionDetails>
        </Accordion>
      )}

      {/* Visual Diagrams Section */}
      <Box sx={{ mb: 3 }}>
        <Typography
          variant="h4"
          sx={{
            mb: 3,
            fontWeight: 700,
            background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
            WebkitBackgroundClip: 'text',
            WebkitTextFillColor: 'transparent',
            display: 'flex',
            alignItems: 'center',
            gap: 1,
          }}
        >
          <DiagramIcon sx={{ fontSize: 40, color: 'primary.main' }} />
          📊 Visual Architecture
        </Typography>

        {/* File Structure Diagram */}
        {analysis.file_structure_diagram && (
          <Box sx={{ mb: 3 }}>
            <MermaidDiagram
              chart={analysis.file_structure_diagram}
              title="📁 Project Structure"
            />
          </Box>
        )}

        {/* Architecture Diagram */}
        {analysis.architecture_diagram && (
          <Box sx={{ mb: 3 }}>
            <MermaidDiagram
              chart={analysis.architecture_diagram}
              title="🏗️ System Architecture"
            />
          </Box>
        )}

        {/* Flow Diagram */}
        {analysis.flow_diagram && (
          <Box sx={{ mb: 3 }}>
            <MermaidDiagram
              chart={analysis.flow_diagram}
              title="🔄 Application Flow"
            />
          </Box>
        )}
      </Box>

      {/* Key Files */}
      {analysis.key_files && analysis.key_files.length > 0 && (
        <Accordion
          sx={{
            mb: 2,
            borderRadius: '12px !important',
            '&:before': { display: 'none' },
            boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
          }}
        >
          <AccordionSummary 
            expandIcon={<ExpandMoreIcon />}
            sx={{
              bgcolor: 'info.light',
              color: 'info.dark',
              borderRadius: '12px 12px 0 0',
              '&:hover': { bgcolor: 'info.main', color: 'white' },
            }}
          >
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
              <FileIcon />
              <Typography variant="h6" sx={{ fontWeight: 600 }}>
                📁 Key Files ({analysis.key_files.length})
              </Typography>
            </Box>
          </AccordionSummary>
          <AccordionDetails sx={{ p: 3 }}>
            <Grid container spacing={2}>
              {analysis.key_files.map((file, index) => (
                <Grid item xs={12} key={index}>
                  <Card 
                    variant="outlined"
                    sx={{ 
                      borderRadius: 2,
                      '&:hover': {
                        boxShadow: 3,
                        transform: 'translateY(-2px)',
                      },
                      transition: 'all 0.2s',
                    }}
                  >
                    <CardContent>
                      <Typography 
                        variant="subtitle1" 
                        sx={{ 
                          fontFamily: 'monospace', 
                          mb: 1,
                          fontWeight: 600,
                          color: 'primary.main',
                        }}
                      >
                        📄 {file.path}
                      </Typography>
                      <Stack direction="row" spacing={1} sx={{ mb: 2 }}>
                        <Chip label={file.type} size="small" color="default" />
                        {file.language && (
                          <Chip label={file.language} size="small" color="primary" />
                        )}
                        <Chip 
                          label={`${file.lines} lines`} 
                          size="small" 
                          variant="outlined" 
                        />
                      </Stack>
                      {file.snippet && (
                        <SyntaxHighlighter
                          language={file.language || 'text'}
                          style={vscDarkPlus}
                          customStyle={{ 
                            fontSize: '0.85rem', 
                            maxHeight: '200px',
                            borderRadius: 8,
                          }}
                        >
                          {file.snippet}
                        </SyntaxHighlighter>
                      )}
                    </CardContent>
                  </Card>
                </Grid>
              ))}
            </Grid>
          </AccordionDetails>
        </Accordion>
      )}

      {/* Dependencies */}
      {analysis.dependencies && analysis.dependencies.length > 0 && (
        <Accordion
          sx={{
            mb: 2,
            borderRadius: '12px !important',
            '&:before': { display: 'none' },
            boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
          }}
        >
          <AccordionSummary 
            expandIcon={<ExpandMoreIcon />}
            sx={{
              bgcolor: 'warning.light',
              color: 'warning.dark',
              borderRadius: '12px 12px 0 0',
              '&:hover': { bgcolor: 'warning.main', color: 'white' },
            }}
          >
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
              <DependencyIcon />
              <Typography variant="h6" sx={{ fontWeight: 600 }}>
                📦 Dependencies
              </Typography>
            </Box>
          </AccordionSummary>
          <AccordionDetails sx={{ p: 3 }}>
            <Stack spacing={3}>
              {analysis.dependencies.map((dep, index) => (
                <Box key={index}>
                  <Typography 
                    variant="subtitle1" 
                    sx={{ 
                      fontFamily: 'monospace', 
                      mb: 1.5,
                      fontWeight: 600,
                      color: 'text.primary',
                    }}
                  >
                    📄 {dep.file}
                  </Typography>
                  <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 1 }}>
                    {Object.entries(dep.dependencies).slice(0, 20).map(([name, version]) => (
                      <Chip
                        key={name}
                        label={`${name}: ${version}`}
                        size="small"
                        variant="outlined"
                        sx={{
                          fontFamily: 'monospace',
                          '&:hover': {
                            bgcolor: 'action.hover',
                          },
                        }}
                      />
                    ))}
                    {Object.keys(dep.dependencies).length > 20 && (
                      <Chip
                        label={`+${Object.keys(dep.dependencies).length - 20} more`}
                        size="small"
                        color="primary"
                      />
                    )}
                  </Box>
                </Box>
              ))}
            </Stack>
          </AccordionDetails>
        </Accordion>
      )}

      {/* Call to action */}
      <Alert 
        severity="success" 
        icon={<CheckCircleIcon />}
        sx={{ 
          mt: 3,
          borderRadius: 3,
          '& .MuiAlert-message': {
            width: '100%',
          },
        }}
      >
        <Typography variant="body1" sx={{ fontWeight: 600, mb: 0.5 }}>
          🎉 Ready to explore!
        </Typography>
        <Typography variant="body2">
          Use the chat interface below to ask questions about this codebase and get instant AI-powered answers.
        </Typography>
      </Alert>
    </Paper>
  );
};

export default OnboardingGuide;

// Made with Bob
