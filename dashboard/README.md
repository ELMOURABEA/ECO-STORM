# ECO-STORM Dashboard

Web-based dashboard for visualizing economic data and analysis results.

## Features

- Real-time economic indicator monitoring
- Interactive charts and visualizations
- Crisis prediction displays
- Risk assessment dashboard
- Historical trend analysis

## Installation

```bash
cd dashboard
npm install
```

## Usage

### Development Mode

```bash
npm run dev
```

### Production Mode

```bash
npm start
```

The dashboard will be available at `http://localhost:3000`

## Configuration

Edit `config.js` to configure:
- API endpoints
- Refresh intervals
- Chart themes
- Display options

## Technologies

- Express.js - Web server
- Chart.js - Data visualization
- Socket.io - Real-time updates
- Axios - HTTP client

## API Integration

The dashboard connects to the ECO-STORM Python backend API to fetch:
- Economic indicator data
- Analysis results
- Predictions
- Alerts

## Development

To contribute to the dashboard:

1. Follow the main [Contributing Guidelines](../CONTRIBUTING.md)
2. Test your changes thoroughly
3. Ensure responsive design
4. Update documentation

## License

GPL-2.0 - See LICENSE file in the root directory
