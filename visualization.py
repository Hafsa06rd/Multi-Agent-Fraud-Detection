# visualization.py
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule, TextElement
from fraud_detection_system import FraudDetectionModel


class ProjectAboutElement(TextElement):
    """About section explaining the project purpose"""

    def render(self, model):
        html = """
        <div style="max-width: 1200px; margin: 0 auto; padding: 0 20px;">
            <div style="background: linear-gradient(135deg, #f8fafc, #e2e8f0); border-radius: 20px; 
                       padding: 40px; margin-bottom: 25px; box-shadow: 0 8px 32px rgba(0,0,0,0.1);
                       border-left: 6px solid #3b82f6;">
                <h2 style="color: #1e40af; margin: 0 0 25px 0; font-size: 26px; text-align: center;
                          display: flex; align-items: center; justify-content: center; gap: 10px;">
                    📖 About This Project
                </h2>

                <div style="display: grid; grid-template-columns: 1fr 2fr; gap: 30px; align-items: center;">
                    <!-- Project Visual -->
                    <div style="text-align: center; background: white; padding: 25px; border-radius: 15px;
                               box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                        <div style="font-size: 72px; margin-bottom: 15px;">🛡️</div>
                        <h3 style="color: #1f2937; margin: 0; font-size: 18px;">Intelligent Agent Fraud Detection System</h3>
                        <p style="color: #6b7280; margin: 10px 0 0 0; font-size: 14px;">Multi-Agent System</p>
                    </div>

                    <!-- Project Description -->
                    <div style="color: #374151; line-height: 1.7; font-size: 16px;">
                        <p style="margin: 0 0 20px 0; font-size: 18px; color: #1f2937; font-weight: 600;">
                            🎯 <strong>Project Purpose:</strong>
                        </p>

                        <p style="margin: 0 0 18px 0;">
                            This project demonstrates an <strong>AI-powered Multi-Agent System</strong> designed to detect 
                            fraudulent credit card transactions in real-time. Using advanced machine learning algorithms 
                            and intelligent agent coordination, the system provides automated fraud detection with 
                            high accuracy and immediate alert capabilities.
                        </p>

                        <p style="margin: 0 0 18px 0;">
                            The system employs <strong>three specialized AI agents</strong> working together: a Data Fetcher 
                            for transaction processing, an AI Fraud Detector using XGBoost machine learning, and a 
                            Notification Sender for real-time alerts. This collaborative approach ensures comprehensive 
                            fraud monitoring while maintaining system efficiency and reliability.
                        </p>

                        <p style="margin: 0 0 20px 0;">
                            <strong>🔬 Technical Innovation:</strong> Built using Mesa framework for multi-agent modeling, 
                            XGBoost for fraud classification, and modern web visualization technologies. The system 
                            processes thousands of transactions per second while providing intuitive dashboards for 
                            both technical teams and business stakeholders.
                        </p>

                        <div style="background: linear-gradient(135deg, #eff6ff, #dbeafe); padding: 15px; 
                                   border-radius: 10px; border-left: 4px solid #3b82f6; margin-top: 20px;">
                            <p style="margin: 0; color: #1e40af; font-weight: 600; font-size: 14px;">
                                💡 <strong>Impact:</strong> This technology helps financial institutions prevent fraud losses, 
                                protect customers, and maintain trust in digital payment systems. The real-time detection 
                                capabilities enable immediate response to suspicious activities, significantly reducing 
                                financial risks and improving overall security.
                            </p>
                        </div>
                    </div>
                </div>

                <!-- Technical Highlights -->
                <div style="margin-top: 30px; display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px;">
                    <div style="background: white; padding: 20px; border-radius: 12px; text-align: center;
                               box-shadow: 0 2px 8px rgba(0,0,0,0.1); border-top: 4px solid #10b981;">
                        <div style="font-size: 32px; margin-bottom: 10px;">🤖</div>
                        <h4 style="color: #10b981; margin: 0 0 8px 0; font-size: 14px; font-weight: bold;">
                            MULTI-AGENT AI
                        </h4>
                        <p style="color: #6b7280; margin: 0; font-size: 12px;">
                            Intelligent agents working in coordination
                        </p>
                    </div>

                    <div style="background: white; padding: 20px; border-radius: 12px; text-align: center;
                               box-shadow: 0 2px 8px rgba(0,0,0,0.1); border-top: 4px solid #f59e0b;">
                        <div style="font-size: 32px; margin-bottom: 10px;">⚡</div>
                        <h4 style="color: #f59e0b; margin: 0 0 8px 0; font-size: 14px; font-weight: bold;">
                            REAL-TIME PROCESSING
                        </h4>
                        <p style="color: #6b7280; margin: 0; font-size: 12px;">
                            Instant fraud detection and alerts
                        </p>
                    </div>

                    <div style="background: white; padding: 20px; border-radius: 12px; text-align: center;
                               box-shadow: 0 2px 8px rgba(0,0,0,0.1); border-top: 4px solid #8b5cf6;">
                        <div style="font-size: 32px; margin-bottom: 10px;">🎯</div>
                        <h4 style="color: #8b5cf6; margin: 0 0 8px 0; font-size: 14px; font-weight: bold;">
                            HIGH ACCURACY
                        </h4>
                        <p style="color: #6b7280; margin: 0; font-size: 12px;">
                            Advanced ML algorithms for precision
                        </p>
                    </div>

                    <div style="background: white; padding: 20px; border-radius: 12px; text-align: center;
                               box-shadow: 0 2px 8px rgba(0,0,0,0.1); border-top: 4px solid #ef4444;">
                        <div style="font-size: 32px; margin-bottom: 10px;">🛡️</div>
                        <h4 style="color: #ef4444; margin: 0 0 8px 0; font-size: 14px; font-weight: bold;">
                            FRAUD PREVENTION
                        </h4>
                        <p style="color: #6b7280; margin: 0; font-size: 12px;">
                            Protecting financial transactions
                        </p>
                    </div>
                </div>
            </div>
        </div>
        """
        return html


class SystemOverviewElement(TextElement):
    """Combined overview with both simple and technical information"""

    def render(self, model):
        step_info = model.get_current_step_info()
        total_messages = len(model.messages)
        metrics = model.get_system_metrics()

        html = f"""
        <div style="max-width: 1200px; margin: 0 auto; padding: 0 20px;">
            <div style="background: linear-gradient(135deg, #4f46e5, #7c3aed); color: white; 
                       padding: 30px; border-radius: 20px; margin-bottom: 25px; text-align: center;
                       box-shadow: 0 10px 40px rgba(79, 70, 229, 0.3);">
                <h1 style="margin: 0 0 15px 0; font-size: 28px; font-weight: bold;">
                    🛡️ Intelligent Agent Credit Card Fraud Detection System
                </h1>
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin: 20px 0;">
                    <div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 10px;">
                        <div style="font-size: 24px; font-weight: bold;">
                            {metrics.get('transactions_processed', 0):,}
                        </div>
                        <div style="font-size: 14px; opacity: 0.9;">Transactions Analyzed</div>
                    </div>
                    <div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 10px;">
                        <div style="font-size: 24px; font-weight: bold;">
                            {metrics.get('frauds_detected', 0)}
                        </div>
                        <div style="font-size: 14px; opacity: 0.9;">Fraud Cases Detected</div>
                    </div>
                    <div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 10px;">
                        <div style="font-size: 24px; font-weight: bold;">
                            {metrics.get('detection_rate', 0):.1%}
                        </div>
                        <div style="font-size: 14px; opacity: 0.9;">Detection Accuracy</div>
                    </div>
                </div>
                <p style="font-size: 18px; margin: 15px 0 5px 0; opacity: 0.95;">
                    🔄 Current Status: {step_info}
                </p>
                <p style="font-size: 14px; margin: 0; opacity: 0.8;">
                    💬 System Communications: {total_messages} | 🔄 Processing Step: {model.step_count}
                </p>
            </div>
        </div>
        """
        return html


class CombinedAgentWorkflowElement(TextElement):
    """Combined technical and simple workflow visualization"""

    def render(self, model):
        states = model.get_agent_states()

        html = """
        <div style="max-width: 1200px; margin: 0 auto; padding: 0 20px;">
            <div style="background: white; border-radius: 20px; padding: 30px; margin-bottom: 25px;
                       box-shadow: 0 8px 32px rgba(0,0,0,0.1);">
                <h2 style="color: #1f2937; margin: 0 0 30px 0; font-size: 24px; text-align: center;">
                    🤖 Agent Activity Dashboard & Workflow
                </h2>
        """

        # Technical Agent Cards
        html += """
                <div style="margin-bottom: 30px;">
                    <h3 style="color: #374151; margin-bottom: 20px; font-size: 18px;">
                        📊 Technical Agent Status
                    </h3>
                    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px;">
        """

        agent_details = [
            {
                'name': 'DataFetcher',
                'title': 'Data Fetcher Agent',
                'icon': '📥',
                'description': 'Loads and validates transaction data'
            },
            {
                'name': 'FraudDetector',
                'title': 'Fraud Detector Agent',
                'icon': '🤖',
                'description': 'AI model for fraud pattern analysis'
            },
            {
                'name': 'NotificationSender',
                'title': 'Notification Sender Agent',
                'icon': '📨',
                'description': 'Generates and sends fraud alerts'
            }
        ]

        status_styles = {
            'idle': {'color': '#6b7280', 'bg': '#f9fafb', 'border': '#e5e7eb'},
            'processing': {'color': '#2563eb', 'bg': '#eff6ff', 'border': '#3b82f6'},
            'waiting': {'color': '#d97706', 'bg': '#fffbeb', 'border': '#f59e0b'},
            'completed': {'color': '#059669', 'bg': '#ecfdf5', 'border': '#10b981'},
            'error': {'color': '#dc2626', 'bg': '#fef2f2', 'border': '#ef4444'}
        }

        for agent in agent_details:
            status = states.get(agent['name'], 'idle')
            style = status_styles.get(status, status_styles['idle'])

            # Get metrics
            metrics_method = getattr(model, f'get_{agent["name"].lower()}_metrics', None)
            metrics = metrics_method() if metrics_method else {}

            html += f"""
                    <div style="background: {style['bg']}; border: 2px solid {style['border']}; 
                               border-radius: 15px; padding: 20px; text-align: center;
                               transition: all 0.3s ease; position: relative;">
                        <div style="font-size: 36px; margin-bottom: 15px;">
                            {agent['icon']}
                        </div>
                        <h4 style="color: {style['color']}; margin: 0 0 10px 0; font-size: 16px; font-weight: bold;">
                            {agent['title']}
                        </h4>
                        <div style="background: {style['color']}; color: white; padding: 6px 12px; 
                                   border-radius: 20px; font-size: 12px; font-weight: bold; margin: 10px 0;
                                   text-transform: uppercase;">
                            {status}
                        </div>
                        <p style="color: #6b7280; font-size: 12px; margin: 10px 0;">
                            {agent['description']}
                        </p>
                        <div style="font-size: 11px; color: #9ca3af; margin-top: 10px;">
                            {self._format_technical_metrics(metrics)}
                        </div>
                    </div>
            """

        # Simple Workflow Steps
        html += """
                    </div>
                </div>

                <div>
                    <h3 style="color: #374151; margin-bottom: 20px; font-size: 18px;">
                        🔄 How The System Works (3 Simple Steps)
                    </h3>
                    <div style="display: flex; justify-content: space-between; align-items: center; gap: 15px;">
        """

        workflow_steps = [
            {
                'step': 1,
                'title': 'Load Data',
                'agent': 'DataFetcher',
                'description': 'Reading credit card transactions',
                'icon': '📥',
                'detail': 'CSV file processing and validation'
            },
            {
                'step': 2,
                'title': 'AI Analysis',
                'agent': 'FraudDetector',
                'description': 'AI checking for fraud patterns',
                'icon': '🤖',
                'detail': 'XGBoost ML model classification'
            },
            {
                'step': 3,
                'title': 'Send Alerts',
                'agent': 'NotificationSender',
                'description': 'Generating fraud notifications',
                'icon': '📨',
                'detail': 'Risk assessment and alert distribution'
            }
        ]

        for i, step in enumerate(workflow_steps):
            status = states.get(step['agent'], 'waiting')
            style = status_styles.get(status, status_styles['waiting'])

            html += f"""
                    <div style="flex: 1; background: {style['bg']}; border: 3px solid {style['border']}; 
                               border-radius: 15px; padding: 20px; text-align: center; position: relative;">

                        <div style="background: {style['color']}; color: white; width: 30px; height: 30px; 
                                   border-radius: 50%; display: flex; align-items: center; justify-content: center;
                                   font-weight: bold; margin: 0 auto 15px auto;">
                            {step['step']}
                        </div>

                        <div style="font-size: 36px; margin-bottom: 15px; 
                                   animation: {'bounce 1s infinite' if status == 'processing' else 'none'};">
                            {step['icon']}
                        </div>

                        <h4 style="color: {style['color']}; margin: 0 0 10px 0; font-size: 16px; font-weight: bold;">
                            {step['title'].upper()}
                        </h4>

                        <p style="color: #4b5563; margin: 0 0 10px 0; font-size: 13px;">
                            {step['description']}
                        </p>

                        <p style="color: #9ca3af; font-size: 11px; margin: 0 0 15px 0; font-style: italic;">
                            {step['detail']}
                        </p>

                        <div style="background: {style['color']}; color: white; padding: 6px 12px; 
                                   border-radius: 15px; font-size: 11px; font-weight: bold;">
                            {status.upper().replace('_', ' ')}
                        </div>
                    </div>
            """

            # Add arrow between steps
            if i < len(workflow_steps) - 1:
                arrow_color = style['color'] if status == 'completed' else '#d1d5db'
                html += f"""
                        <div style="display: flex; align-items: center; color: {arrow_color}; font-size: 24px;">
                            {'🔄' if status == 'completed' else '▶️'}
                        </div>
                """

        html += """
                    </div>
                </div>
            </div>
        </div>
        <style>
            @keyframes bounce {
                0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
                40% { transform: translateY(-8px); }
                60% { transform: translateY(-4px); }
            }
        </style>
        """

        return html

    def _format_technical_metrics(self, metrics):
        if not metrics:
            return "No metrics available"

        formatted = []
        for key, value in metrics.items():
            if key == 'last_activity':
                formatted.append(f"Last: {value}")
            elif isinstance(value, (int, float)):
                formatted.append(f"{key.replace('_', ' ').title()}: {value}")
            else:
                formatted.append(f"{key.replace('_', ' ').title()}: {str(value)[:12]}")

        return "<br>".join(formatted[:3])


class CombinedCommunicationElement(TextElement):
    """Combined technical and simple communication visualization"""

    def render(self, model):
        if not hasattr(model, 'messages') or not model.messages:
            return """
            <div style="max-width: 1200px; margin: 0 auto; padding: 0 20px;">
                <div style="background: linear-gradient(135deg, #f8fafc, #e2e8f0); border-radius: 20px; 
                           padding: 40px; text-align: center; margin: 25px 0;">
                    <h2 style="color: #475569; margin-bottom: 20px;">💬 System Communication</h2>
                    <div style="font-size: 64px; margin: 25px 0; opacity: 0.3;">🔄</div>
                    <p style="color: #64748b; font-size: 18px;">Waiting for agents to start communicating...</p>
                </div>
            </div>
            """

        messages = model.messages[-6:]

        html = """
        <div style="max-width: 1200px; margin: 0 auto; padding: 0 20px;">
            <div style="background: white; border-radius: 20px; padding: 30px; margin-bottom: 25px;
                       box-shadow: 0 8px 32px rgba(0,0,0,0.1);">
                <h2 style="color: #1f2937; margin: 0 0 30px 0; font-size: 24px; text-align: center;">
                    💬 Inter-Agent Communication Network
                </h2>
        """

        # Visual Network Diagram
        html += self._create_network_diagram(model)

        # Communication Timeline
        html += """
                <div style="margin-top: 30px;">
                    <h3 style="color: #374151; margin-bottom: 20px; font-size: 18px;">
                        📋 Real-Time Communication Log
                    </h3>
                    <div style="max-height: 400px; overflow-y: auto; background: #f9fafb; 
                               border-radius: 15px; padding: 20px;">
        """

        for i, msg in enumerate(reversed(messages)):
            message_info = self._get_message_info(msg)

            html += f"""
                    <div style="background: white; border-left: 4px solid {message_info['color']}; 
                               border-radius: 0 10px 10px 0; padding: 15px; margin: 10px 0;
                               box-shadow: 0 2px 8px rgba(0,0,0,0.1); 
                               animation: slideIn 0.5s ease-in-out {i * 0.1}s both;">

                        <div style="display: flex; justify-content: between; align-items: start; gap: 15px;">
                            <div style="font-size: 24px; color: {message_info['color']};">
                                {message_info['icon']}
                            </div>
                            <div style="flex: 1;">
                                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                                    <span style="font-weight: bold; color: {message_info['color']}; font-size: 14px;">
                                        {msg.sender} → {msg.receiver}
                                    </span>
                                    <span style="background: {message_info['color']}; color: white; 
                                               padding: 2px 8px; border-radius: 10px; font-size: 11px; font-weight: bold;">
                                        {msg.message_type.replace('_', ' ').upper()}
                                    </span>
                                </div>
                                <div style="color: #4b5563; font-size: 14px; margin-bottom: 5px;">
                                    <strong>Simple:</strong> {message_info['simple_desc']}
                                </div>
                                <div style="color: #6b7280; font-size: 12px; margin-bottom: 8px;">
                                    <strong>Technical:</strong> {message_info['technical_desc']}
                                </div>
                                <div style="color: #9ca3af; font-size: 11px;">
                                    🕒 {msg.timestamp}
                                </div>
                            </div>
                        </div>
                    </div>
            """

        html += """
                    </div>
                </div>
            </div>
        </div>
        <style>
            @keyframes slideIn {
                from { opacity: 0; transform: translateX(-20px); }
                to { opacity: 1; transform: translateX(0); }
            }
        </style>
        """

        return html

    def _create_network_diagram(self, model):
        """Create visual network of agents"""
        states = model.get_agent_states()

        status_colors = {
            'idle': '#6b7280',
            'processing': '#3b82f6',
            'waiting': '#f59e0b',
            'completed': '#10b981',
            'error': '#ef4444'
        }

        html = """
        <div style="background: linear-gradient(135deg, #f1f5f9, #e2e8f0); border-radius: 15px; 
                   padding: 30px; position: relative; overflow: hidden;">
            <div style="display: flex; justify-content: space-around; align-items: center; position: relative;">
        """

        agents = [
            {'name': 'DataFetcher', 'label': 'Data\nFetcher', 'icon': '📥'},
            {'name': 'FraudDetector', 'label': 'Fraud\nDetector', 'icon': '🤖'},
            {'name': 'NotificationSender', 'label': 'Notification\nSender', 'icon': '📨'}
        ]

        for agent in agents:
            status = states.get(agent['name'], 'idle')
            color = status_colors.get(status, '#6b7280')

            html += f"""
            <div style="display: flex; flex-direction: column; align-items: center; z-index: 10; position: relative;">
                <div style="width: 100px; height: 100px; border-radius: 50%; 
                           background: linear-gradient(135deg, {color}, {color}dd);
                           display: flex; flex-direction: column; align-items: center; justify-content: center;
                           color: white; font-weight: bold; font-size: 12px; text-align: center;
                           box-shadow: 0 8px 16px rgba(0,0,0,0.2); border: 4px solid white;
                           animation: pulse 2s infinite;">
                    <div style="font-size: 24px; margin-bottom: 5px;">{agent['icon']}</div>
                    <div style="line-height: 1.2;">{agent['label']}</div>
                </div>
                <div style="margin-top: 10px; background: {color}; color: white; 
                           padding: 4px 12px; border-radius: 15px; font-size: 11px; font-weight: bold;">
                    {status.upper()}
                </div>
            </div>
            """

        # Add connecting lines
        if model.messages:
            html += """
            <svg style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1;">
                <defs>
                    <linearGradient id="flowGradient" x1="0%" y1="0%" x2="100%" y2="0%">
                        <stop offset="0%" style="stop-color:#3b82f6;stop-opacity:0.3"/>
                        <stop offset="50%" style="stop-color:#3b82f6;stop-opacity:1"/>
                        <stop offset="100%" style="stop-color:#10b981;stop-opacity:0.3"/>
                    </linearGradient>
                </defs>
                <line x1="15%" y1="50%" x2="85%" y2="50%" stroke="url(#flowGradient)" 
                      stroke-width="6" opacity="0.8">
                    <animate attributeName="stroke-dasharray" values="0,200;100,100;200,0" 
                             dur="3s" repeatCount="indefinite"/>
                </line>
            </svg>
            """

        html += """
            </div>
        </div>
        <style>
            @keyframes pulse {
                0%, 100% { box-shadow: 0 8px 16px rgba(0,0,0,0.2); }
                50% { box-shadow: 0 12px 24px rgba(59,130,246,0.4); }
            }
        </style>
        """

        return html

    def _get_message_info(self, msg):
        """Get both simple and technical descriptions"""
        message_types = {
            'data_ready': {
                'simple_desc': 'Transaction data has been loaded and is ready for analysis',
                'technical_desc': 'CSV file parsed, data validated, statistics computed',
                'icon': '📥',
                'color': '#3b82f6'
            },
            'fraud_detection': {
                'simple_desc': 'AI has found suspicious transactions and is sending details',
                'technical_desc': 'XGBoost model predictions complete, feature importance calculated',
                'icon': '🚨',
                'color': '#ef4444'
            },
            'notification_complete': {
                'simple_desc': 'All fraud alerts have been successfully sent to security team',
                'technical_desc': 'Notification processing complete, alerts queued for delivery',
                'icon': '📨',
                'color': '#10b981'
            }
        }

        return message_types.get(msg.message_type, {
            'simple_desc': 'System communication between agents',
            'technical_desc': 'Internal agent message passing',
            'icon': '🔄',
            'color': '#6b7280'
        })


class CombinedMetricsElement(TextElement):
    """Combined simple and technical metrics"""

    def render(self, model):
        metrics = model.get_system_metrics()

        html = """
        <div style="max-width: 1200px; margin: 0 auto; padding: 0 20px;">
            <div style="background: white; border-radius: 20px; padding: 30px; margin-bottom: 25px;
                       box-shadow: 0 8px 32px rgba(0,0,0,0.1);">
                <h2 style="color: #1f2937; margin: 0 0 30px 0; font-size: 24px; text-align: center;">
                    📊 System Performance Dashboard
                </h2>

                <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px;">
        """

        metric_configs = [
            {
                'title': 'Transactions Processed',
                'simple_title': 'Credit Cards Checked',
                'value': f"{metrics.get('transactions_processed', 0):,}",
                'icon': '💳',
                'color': '#3b82f6',
                'explanation': 'Total transactions analyzed by AI system'
            },
            {
                'title': 'Fraud Cases Detected',
                'simple_title': 'Suspicious Transactions',
                'value': f"{metrics.get('frauds_detected', 0)}",
                'icon': '🚨',
                'color': '#ef4444',
                'explanation': 'High-risk transactions flagged for review'
            },
            {
                'title': 'Detection Rate',
                'simple_title': 'AI Accuracy',
                'value': f"{metrics.get('detection_rate', 0):.1%}",
                'icon': '🎯',
                'color': '#10b981',
                'explanation': 'Percentage of fraud cases successfully identified'
            },
            {
                'title': 'Processing Speed',
                'simple_title': 'System Speed',
                'value': f"{metrics.get('processing_speed', 0):.0f}/sec",
                'icon': '⚡',
                'color': '#f59e0b',
                'explanation': 'Transactions processed per second'
            }
        ]

        for metric in metric_configs:
            html += f"""
                <div style="background: linear-gradient(135deg, {metric['color']}15, {metric['color']}08); 
                           border: 2px solid {metric['color']}; border-radius: 15px; padding: 25px; 
                           text-align: center; position: relative; overflow: hidden;
                           transition: transform 0.3s ease;">

                    <div style="font-size: 42px; margin-bottom: 15px; animation: float 3s ease-in-out infinite;">
                        {metric['icon']}
                    </div>

                    <h4 style="color: {metric['color']}; margin: 0 0 5px 0; font-size: 13px; 
                              text-transform: uppercase; letter-spacing: 1px; font-weight: bold;">
                        {metric['title']}
                    </h4>

                    <h5 style="color: #6b7280; margin: 0 0 15px 0; font-size: 12px; font-weight: normal;">
                        ({metric['simple_title']})
                    </h5>

                    <p style="font-size: 32px; font-weight: bold; color: {metric['color']}; 
                              margin: 15px 0; font-family: 'Courier New', monospace;">
                        {metric['value']}
                    </p>

                    <p style="font-size: 11px; color: #6b7280; margin: 0; line-height: 1.4;">
                        {metric['explanation']}
                    </p>

                    <div style="position: absolute; top: 10px; right: 10px; width: 12px; height: 12px; 
                               background: {metric['color']}; border-radius: 50%; opacity: 0.6;
                               animation: pulse 2s infinite;">
                    </div>
                </div>
            """

        html += """
                </div>
            </div>
        </div>
        <style>
            @keyframes float {
                0%, 100% { transform: translateY(0px); }
                50% { transform: translateY(-8px); }
            }
            @keyframes pulse {
                0%, 100% { opacity: 0.6; transform: scale(1); }
                50% { opacity: 1; transform: scale(1.2); }
            }
        </style>
        """

        return html


class CombinedTransactionElement(TextElement):
    """Combined transaction processing view"""

    def render(self, model):
        current_transactions = getattr(model, 'current_transactions', [])

        html = """
        <div style="max-width: 1200px; margin: 0 auto; padding: 0 20px;">
            <div style="background: white; border-radius: 20px; padding: 30px; margin-bottom: 25px;
                       box-shadow: 0 8px 32px rgba(0,0,0,0.1);">
                <h2 style="color: #1f2937; margin: 0 0 30px 0; font-size: 24px; text-align: center;">
                    🔄 Transaction Processing Monitor
                </h2>
        """

        if not current_transactions:
            status_message = "⏳ System ready to analyze transactions"
            if model.fraud_detector.status == "processing":
                status_message = "🔄 AI is currently analyzing transactions for fraud patterns..."
            elif model.fraud_detector.status == "completed":
                status_message = "✅ Transaction analysis completed successfully"

            html += f"""
                <div style="background: linear-gradient(135deg, #f0f9ff, #e0f2fe); border-radius: 15px; 
                           padding: 40px; text-align: center; border: 2px solid #0ea5e9;">
                    <div style="font-size: 64px; margin: 25px 0; opacity: 0.6;">🏦</div>
                    <p style="color: #0c4a6e; font-size: 18px; margin: 0;">{status_message}</p>
                </div>
            """
        else:
            html += """
                <div style="background: #f8fafc; border-radius: 15px; overflow: hidden;">
                    <div style="background: linear-gradient(135deg, #1e40af, #3b82f6); color: white; 
                               padding: 20px; text-align: center;">
                        <h3 style="margin: 0; font-size: 18px;">
                            🚨 High-Risk Transactions Detected ({len(current_transactions)} total)
                        </h3>
                    </div>
                    <div style="max-height: 400px; overflow-y: auto; padding: 20px;">
            """

            for i, transaction in enumerate(current_transactions[:12]):
                risk_info = self._get_risk_info(transaction.get('risk_score', 0))

                html += f"""
                    <div style="background: white; border: 2px solid {risk_info['color']}; 
                               border-radius: 15px; padding: 20px; margin: 15px 0;
                               animation: alertPulse 0.8s ease-in-out {i * 0.1}s both;
                               box-shadow: 0 4px 12px rgba(0,0,0,0.1);">

                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <div style="display: flex; align-items: center; gap: 15px;">
                                <div style="font-size: 32px;">{risk_info['icon']}</div>
                                <div>
                                    <h4 style="color: #1f2937; margin: 0 0 5px 0; font-size: 16px; font-weight: bold;">
                                        Transaction ID: {transaction.get('id', 'Unknown')}
                                    </h4>
                                    <p style="color: #6b7280; margin: 0; font-size: 14px;">
                                        Amount: <span style="font-weight: bold; color: {risk_info['color']};">
                                        ${transaction.get('amount', 0):,.2f}</span>
                                    </p>
                                </div>
                            </div>
                            <div style="text-align: right;">
                                <div style="background: {risk_info['color']}; color: white; 
                                           padding: 8px 16px; border-radius: 20px; font-size: 12px; 
                                           font-weight: bold; margin-bottom: 5px;">
                                    {risk_info['label']}
                                </div>
                                <div style="color: #6b7280; font-size: 11px;">
                                    Risk Score: {transaction.get('risk_score', 0):.0%}
                                </div>
                            </div>
                        </div>

                        <div style="margin-top: 15px; padding: 12px; background: {risk_info['bg']}; 
                                   border-radius: 8px; border-left: 4px solid {risk_info['color']};">
                            <p style="margin: 0; color: #374151; font-size: 13px;">
                                <strong>🔍 Analysis:</strong> {risk_info['description']}
                            </p>
                        </div>
                    </div>
                """

            html += """
                    </div>
                </div>
            """

        html += """
            </div>
        </div>
        <style>
            @keyframes alertPulse {
                from { opacity: 0; transform: scale(0.95); }
                to { opacity: 1; transform: scale(1); }
            }
        </style>
        """

        return html

    def _get_risk_info(self, risk_score):
        if risk_score >= 0.8:
            return {
                'label': 'CRITICAL RISK',
                'color': '#dc2626',
                'bg': '#fef2f2',
                'icon': '🔴',
                'description': 'Extremely high probability of fraud - immediate action required'
            }
        elif risk_score >= 0.6:
            return {
                'label': 'HIGH RISK',
                'color': '#ea580c',
                'bg': '#fff7ed',
                'icon': '🟠',
                'description': 'Strong fraud indicators detected - recommend manual review'
            }
        else:
            return {
                'label': 'MODERATE RISK',
                'color': '#ca8a04',
                'bg': '#fffbeb',
                'icon': '🟡',
                'description': 'Some suspicious patterns found - monitor closely'
            }


class CenteredChartsElement(TextElement):
    """Custom centered charts replacing Mesa's default charts"""

    def render(self, model):
        metrics = model.get_system_metrics()

        # Get data for charts
        fraud_data = []
        processing_data = []

        # Create sample data points for visualization
        steps = min(model.step_count, 10)
        for i in range(steps):
            step_frauds = len(model.notifications) if i == steps - 1 else int(
                len(model.notifications) * (i + 1) / steps)
            step_processed = metrics.get('transactions_processed', 0) if i == steps - 1 else int(
                metrics.get('transactions_processed', 0) * (i + 1) / steps)

            fraud_data.append({'step': i + 1, 'value': step_frauds})
            processing_data.append({'step': i + 1, 'value': step_processed})

        html = f"""
        <div style="max-width: 1200px; margin: 0 auto; padding: 0 20px;">
            <div style="background: white; border-radius: 20px; padding: 30px; margin-bottom: 25px;
                       box-shadow: 0 8px 32px rgba(0,0,0,0.1);">
                <h2 style="color: #1f2937; margin: 0 0 30px 0; font-size: 24px; text-align: center;">
                    📈 System Performance Charts
                </h2>

                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">

                    <!-- Fraud Detection Chart -->
                    <div style="background: #fef2f2; border: 2px solid #dc2626; border-radius: 15px; padding: 20px;">
                        <h3 style="color: #dc2626; margin: 0 0 20px 0; text-align: center; font-size: 18px;">
                            🚨 Fraud Detection Progress
                        </h3>
                        <div style="position: relative; height: 200px;">
                            {self._create_fraud_chart(fraud_data)}
                        </div>
                        <div style="text-align: center; margin-top: 15px;">
                            <span style="background: #dc2626; color: white; padding: 8px 16px; 
                                       border-radius: 20px; font-size: 14px; font-weight: bold;">
                                Total Alerts: {len(model.notifications)}
                            </span>
                        </div>
                    </div>

                    <!-- Transaction Processing Chart -->
                    <div style="background: #eff6ff; border: 2px solid #3b82f6; border-radius: 15px; padding: 20px;">
                        <h3 style="color: #3b82f6; margin: 0 0 20px 0; text-align: center; font-size: 18px;">
                            💳 Transaction Processing
                        </h3>
                        <div style="position: relative; height: 200px;">
                            {self._create_processing_chart(processing_data)}
                        </div>
                        <div style="text-align: center; margin-top: 15px;">
                            <span style="background: #3b82f6; color: white; padding: 8px 16px; 
                                       border-radius: 20px; font-size: 14px; font-weight: bold;">
                                Total Processed: {metrics.get('transactions_processed', 0):,}
                            </span>
                        </div>
                    </div>
                </div>

                <!-- Combined Performance Overview -->
                <div style="margin-top: 30px; background: linear-gradient(135deg, #f8fafc, #e2e8f0); 
                           border-radius: 15px; padding: 25px;">
                    <h3 style="color: #374151; margin: 0 0 20px 0; text-align: center; font-size: 18px;">
                        📊 Real-Time System Performance
                    </h3>
                    <div style="height: 150px; position: relative;">
                        {self._create_combined_chart(fraud_data, processing_data)}
                    </div>
                </div>
            </div>
        </div>
        """

        return html

    def _create_fraud_chart(self, data):
        if not data:
            return '<div style="text-align: center; padding: 50px; color: #9ca3af;">No fraud data yet</div>'

        max_value = max([d['value'] for d in data]) if data else 1

        html = """
        <svg width="100%" height="100%" viewBox="0 0 400 200" style="overflow: visible;">
            <defs>
                <linearGradient id="fraudGradient" x1="0%" y1="0%" x2="0%" y2="100%">
                    <stop offset="0%" style="stop-color:#dc2626;stop-opacity:0.8"/>
                    <stop offset="100%" style="stop-color:#dc2626;stop-opacity:0.2"/>
                </linearGradient>
            </defs>
        """

        # Create bars
        bar_width = 350 / len(data) if data else 50
        for i, point in enumerate(data):
            height = (point['value'] / max_value * 160) if max_value > 0 else 0
            x = 25 + i * bar_width 
            y = 180 - height

            html += f"""
            <rect x="{x}" y="{y}" width="{bar_width * 0.8}" height="{height}" 
                  fill="url(#fraudGradient)" rx="4" ry="4">
                <animate attributeName="height" from="0" to="{height}" dur="1s" begin="{i * 0.1}s"/>
                <animate attributeName="y" from="180" to="{y}" dur="1s" begin="{i * 0.1}s"/>
            </rect>
            <text x="{x + bar_width * 0.4}" y="195" text-anchor="middle" 
                  font-size="12" fill="#6b7280">{point['step']}</text>
            <text x="{x + bar_width * 0.4}" y="{y - 5}" text-anchor="middle" 
                  font-size="11" font-weight="bold" fill="#dc2626">{point['value']}</text>
            """

        html += "</svg>"
        return html

    def _create_processing_chart(self, data):
        if not data:
            return '<div style="text-align: center; padding: 50px; color: #9ca3af;">No processing data yet</div>'

        max_value = max([d['value'] for d in data]) if data else 1

        html = """
        <svg width="100%" height="100%" viewBox="0 0 400 200" style="overflow: visible;">
            <defs>
                <linearGradient id="processingGradient" x1="0%" y1="0%" x2="100%" y2="0%">
                    <stop offset="0%" style="stop-color:#3b82f6;stop-opacity:0.8"/>
                    <stop offset="100%" style="stop-color:#1d4ed8;stop-opacity:1"/>
                </linearGradient>
            </defs>
        """

        # Create line chart
        points = []
        for i, point in enumerate(data):
            x = 25 + (i * 350 / (len(data) - 1)) if len(data) > 1 else 200
            y = 180 - (point['value'] / max_value * 160) if max_value > 0 else 180
            points.append(f"{x},{y}")

            # Add points
            html += f"""
            <circle cx="{x}" cy="{y}" r="6" fill="#3b82f6" stroke="white" stroke-width="2">
                <animate attributeName="r" from="0" to="6" dur="0.5s" begin="{i * 0.1}s"/>
            </circle>
            <text x="{x}" y="195" text-anchor="middle" font-size="12" fill="#6b7280">{point['step']}</text>
            <text x="{x}" y="{y - 15}" text-anchor="middle" font-size="11" 
                  font-weight="bold" fill="#3b82f6">{point['value']:,}</text>
            """

        # Add line
        if len(points) > 1:
            path = "M " + " L ".join(points)
            html += f"""
            <path d="{path}" stroke="url(#processingGradient)" stroke-width="3" 
                  fill="none" stroke-dasharray="1000" stroke-dashoffset="1000">
                <animate attributeName="stroke-dashoffset" from="1000" to="0" dur="2s"/>
            </path>
            """

        html += "</svg>"
        return html

    def _create_combined_chart(self, fraud_data, processing_data):
        html = """
        <div style="display: flex; justify-content: space-around; align-items: end; height: 100%; padding: 20px;">
        """

        # Fraud indicator
        fraud_count = len(fraud_data)
        fraud_height = min(fraud_count * 10, 100)

        # Processing indicator
        processing_count = len(processing_data)
        processing_height = min(processing_count * 10, 100)

        html += f"""
            <div style="text-align: center;">
                <div style="width: 60px; height: {fraud_height}px; background: linear-gradient(to top, #dc2626, #fca5a5); 
                           border-radius: 8px; margin: 0 auto 10px auto; position: relative;
                           animation: growUp 1s ease-out;">
                    <div style="position: absolute; top: -25px; left: 50%; transform: translateX(-50%);
                               background: #dc2626; color: white; padding: 4px 8px; border-radius: 10px;
                               font-size: 12px; font-weight: bold;">{fraud_count}</div>
                </div>
                <div style="font-size: 14px; color: #dc2626; font-weight: bold;">Fraud Alerts</div>
            </div>

            <div style="text-align: center;">
                <div style="width: 60px; height: {processing_height}px; background: linear-gradient(to top, #3b82f6, #93c5fd); 
                           border-radius: 8px; margin: 0 auto 10px auto; position: relative;
                           animation: growUp 1.2s ease-out;">
                    <div style="position: absolute; top: -25px; left: 50%; transform: translateX(-50%);
                               background: #3b82f6; color: white; padding: 4px 8px; border-radius: 10px;
                               font-size: 12px; font-weight: bold;">{processing_count}</div>
                </div>
                <div style="font-size: 14px; color: #3b82f6; font-weight: bold;">Processing Steps</div>
            </div>
        """

        html += """
        </div>
        <style>
            @keyframes growUp {
                from { height: 0; }
                to { height: var(--final-height); }
            }
        </style>
        """

        return html


class CombinedFraudAlertsElement(TextElement):
    """Combined fraud alerts with both simple and detailed views"""

    def render(self, model):
        if not hasattr(model, 'notifications') or not model.notifications:
            return """
            <div style="max-width: 1200px; margin: 0 auto; padding: 0 20px;">
                <div style="background: linear-gradient(135deg, #fef3f2, #fee2e2); border: 3px dashed #fca5a5; 
                           border-radius: 20px; padding: 50px; text-align: center; margin: 25px 0;">
                    <h2 style="color: #dc2626; margin-bottom: 20px;">🛡️ Fraud Alert Center</h2>
                    <div style="font-size: 72px; margin: 30px 0; opacity: 0.4;">🔍</div>
                    <p style="color: #7f1d1d; font-size: 18px; margin-bottom: 10px;">
                        No suspicious transactions detected yet.
                    </p>
                    <p style="color: #991b1b; font-size: 16px;">
                        Intelligent Agent system is actively monitoring all transactions for fraud patterns.
                    </p>
                </div>
            </div>
            """

        notifications = model.notifications
        recent_alerts = notifications[-10:] if len(notifications) > 10 else notifications
        total_risk_amount = sum(alert['amount'] for alert in notifications)

        html = f"""
        <div style="max-width: 1200px; margin: 0 auto; padding: 0 20px;">
            <div style="background: white; border-radius: 20px; padding: 30px; margin-bottom: 25px;
                       box-shadow: 0 8px 32px rgba(0,0,0,0.1);">
                <h2 style="color: #dc2626; margin: 0 0 30px 0; font-size: 24px; text-align: center;">
                    🚨 Fraud Detection Alert Center
                </h2>

                <!-- Alert Summary -->
                <div style="background: linear-gradient(135deg, #fef2f2, #fee2e2); padding: 25px; 
                           border-radius: 15px; margin-bottom: 30px; border-left: 6px solid #dc2626;">
                    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; text-align: center;">
                        <div>
                            <div style="font-size: 28px; color: #dc2626; font-weight: bold;">
                                {len(notifications)}
                            </div>
                            <div style="font-size: 13px; color: #7f1d1d; font-weight: bold;">TOTAL ALERTS</div>
                        </div>
                        <div>
                            <div style="font-size: 28px; color: #dc2626; font-weight: bold;">
                                ${total_risk_amount:,.0f}
                            </div>
                            <div style="font-size: 13px; color: #7f1d1d; font-weight: bold;">$ AT RISK</div>
                        </div>
                        <div>
                            <div style="font-size: 28px; color: #dc2626; font-weight: bold;">
                                {max((alert.get('confidence', 0.8) for alert in notifications), default=0):.0%}
                            </div>
                            <div style="font-size: 13px; color: #7f1d1d; font-weight: bold;">MAX CONFIDENCE</div>
                        </div>
                        <div>
                            <div style="font-size: 28px; color: #dc2626; font-weight: bold;">
                                {len([a for a in notifications if a['amount'] > 1000])}
                            </div>
                            <div style="font-size: 13px; color: #7f1d1d; font-weight: bold;">HIGH VALUE</div>
                        </div>
                    </div>
                </div>

                <!-- Individual Alerts -->
                <div style="max-height: 600px; overflow-y: auto;">
        """

        for i, alert in enumerate(reversed(recent_alerts)):
            severity = self._get_alert_severity(alert)

            html += f"""
                <div style="background: {severity['bg']}; border: 2px solid {severity['color']}; 
                           border-radius: 15px; padding: 25px; margin: 20px 0;
                           animation: alertSlideIn 0.6s ease-in-out {i * 0.1}s both;
                           box-shadow: 0 6px 20px rgba(0,0,0,0.1);">

                    <!-- Alert Header -->
                    <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 20px;">
                        <div>
                            <h3 style="color: {severity['color']}; margin: 0 0 8px 0; font-size: 18px;">
                                {severity['icon']} FRAUD ALERT #{len(notifications) - len(recent_alerts) + len(recent_alerts) - i}
                            </h3>
                            <div style="display: flex; gap: 10px; align-items: center;">
                                <span style="background: {severity['color']}; color: white; padding: 6px 14px; 
                                           border-radius: 20px; font-size: 12px; font-weight: bold;">
                                    {severity['level']}
                                </span>
                                <span style="background: white; color: {severity['color']}; padding: 6px 14px; 
                                           border-radius: 20px; font-size: 12px; font-weight: bold; border: 2px solid {severity['color']};">
                                    {alert.get('confidence', 0.8):.0%} CONFIDENCE
                                </span>
                            </div>
                        </div>
                        <div style="text-align: right;">
                            <div style="color: {severity['color']}; font-weight: bold; font-size: 13px;">
                                {severity['action']}
                            </div>
                            <div style="color: #6b7280; font-size: 12px; margin-top: 5px;">
                                🕒 {alert['timestamp']}
                            </div>
                        </div>
                    </div>

                    <!-- Transaction Details -->
                    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; margin-bottom: 20px;">
                        <div style="background: white; padding: 15px; border-radius: 10px; text-align: center;">
                            <div style="color: #6b7280; font-size: 12px; font-weight: bold; margin-bottom: 5px;">
                                💰 TRANSACTION AMOUNT
                            </div>
                            <div style="font-size: 24px; color: {severity['color']}; font-weight: bold;">
                                ${alert['amount']:,.2f}
                            </div>
                        </div>
                        <div style="background: white; padding: 15px; border-radius: 10px; text-align: center;">
                            <div style="color: #6b7280; font-size: 12px; font-weight: bold; margin-bottom: 5px;">
                                ⏰ TRANSACTION TIME
                            </div>
                            <div style="font-size: 18px; color: #374151; font-weight: bold;">
                                {alert['time']:.0f}
                            </div>
                        </div>
                        <div style="background: white; padding: 15px; border-radius: 10px; text-align: center;">
                            <div style="color: #6b7280; font-size: 12px; font-weight: bold; margin-bottom: 5px;">
                                🔍 RISK INDICATORS
                            </div>
                            <div style="font-size: 18px; color: #374151; font-weight: bold;">
                                {len(alert.get('top_indicators', []))} Found
                            </div>
                        </div>
                    </div>

                    <!-- Risk Indicators -->
                    <div style="background: white; border-radius: 12px; padding: 20px; margin-bottom: 20px;">
                        <h4 style="color: {severity['color']}; margin: 0 0 15px 0; font-size: 16px;">
                            🔍 AI-Detected Risk Factors:
                        </h4>
                        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px;">
            """

            for feature, importance in alert.get('top_indicators', []):
                indicator_color = '#dc2626' if importance > 0.1 else '#ea580c' if importance > 0.05 else '#f59e0b'
                html += f"""
                            <div style="background: {indicator_color}15; border: 2px solid {indicator_color}; 
                                       border-radius: 10px; padding: 12px; text-align: center;">
                                <div style="font-size: 12px; color: {indicator_color}; font-weight: bold; 
                                           text-transform: uppercase; margin-bottom: 8px;">
                                    {feature.replace('_', ' ')[:15]}
                                </div>
                                <div style="font-size: 16px; color: {indicator_color}; font-weight: bold; margin-bottom: 8px;">
                                    {importance:.4f}
                                </div>
                                <div style="background: {indicator_color}; height: 4px; border-radius: 2px; 
                                           width: {min(importance * 1000, 100)}%; margin: 0 auto;"></div>
                            </div>
                """

            html += f"""
                        </div>
                    </div>

                    <!-- Recommended Actions -->
                    <div style="background: linear-gradient(135deg, #eff6ff, #dbeafe); padding: 18px; 
                               border-radius: 10px; border-left: 4px solid #3b82f6;">
                        <h4 style="color: #1e40af; margin: 0 0 12px 0; font-size: 14px; font-weight: bold;">
                            📋 IMMEDIATE ACTION REQUIRED:
                        </h4>
                        <div style="color: #374151; font-size: 13px; line-height: 1.6;">
                            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px;">
                                <div>
                                    <strong>🔒 Security Team:</strong><br>
                                    • Contact cardholder immediately<br>
                                    • Freeze account if confirmed fraud<br>
                                    • Document investigation details
                                </div>
                                <div>
                                    <strong>📊 Risk Management:</strong><br>
                                    • Review recent transaction patterns<br>
                                    • Update fraud detection rules<br>
                                    • Monitor for similar cases
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            """

        html += """
                </div>
            </div>
        </div>
        <style>
            @keyframes alertSlideIn {
                from { opacity: 0; transform: translateY(30px); }
                to { opacity: 1; transform: translateY(0); }
            }
        </style>
        """

        return html

    def _get_alert_severity(self, alert):
        amount = alert['amount']
        confidence = alert.get('confidence', 0.8)

        if amount > 1000 or confidence > 0.9:
            return {
                'level': 'CRITICAL RISK',
                'color': '#dc2626',
                'bg': '#fef2f2',
                'icon': '🔴',
                'action': 'IMMEDIATE ACTION REQUIRED'
            }
        elif amount > 500 or confidence > 0.8:
            return {
                'level': 'HIGH RISK',
                'color': '#ea580c',
                'bg': '#fff7ed',
                'icon': '🟠',
                'action': 'REVIEW WITHIN 1 HOUR'
            }
        else:
            return {
                'level': 'MEDIUM RISK',
                'color': '#f59e0b',
                'bg': '#fffbeb',
                'icon': '🟡',
                'action': 'REVIEW WITHIN 24 HOURS'
            }


def create_enhanced_fraud_detection_visualization():
    """Create and launch the comprehensive visualization server"""

    # Create combined visualization elements
    about_section = ProjectAboutElement()  # NEW: About section explaining project purpose
    system_overview = SystemOverviewElement()
    workflow = CombinedAgentWorkflowElement()
    communication = CombinedCommunicationElement()
    metrics = CombinedMetricsElement()
    charts = CenteredChartsElement()  # Custom centered charts
    transactions = CombinedTransactionElement()
    alerts = CombinedFraudAlertsElement()

    # Create and configure server with properly centered layout
    server = ModularServer(
        FraudDetectionModel,
        [
            about_section,  # About the project (NEW)
            system_overview,  # System overview with key metrics
            workflow,  # Combined agent workflow (technical + simple)
            communication,  # Inter-agent communication network
            metrics,  # Performance metrics dashboard
            charts,  # Custom centered charts
            transactions,  # Transaction processing monitor
            alerts  # Comprehensive fraud alerts
        ],
        "🛡️ Intelligent Agent Fraud Detection System - Comprehensive Dashboard"
    )

    return server


if __name__ == "__main__":
    print("🚀 Starting Comprehensive Fraud Detection Dashboard...")
    print("=" * 80)
    print("✨ ENHANCED DASHBOARD FEATURES:")
    print("  📖 Project purpose and technical overview")
    print("  🎯 Perfect for both technical and non-technical users")
    print("  📊 Simple explanations + detailed technical information")
    print("  🤖 Real-time agent workflow visualization")
    print("  💬 Inter-agent communication network")
    print("  🚨 Comprehensive fraud alert system")
    print("  📈 Custom centered performance charts")
    print("  🎨 Professional, fully centered layout")
    print("  ⚡ Multiple individual fraud notifications")
    print("  📱 Responsive design for all devices")
    print("=" * 80)

    server = create_enhanced_fraud_detection_visualization()
    print("\n🌐 Open your web browser and navigate to: http://127.0.0.1:8521")
    print("📱 Responsive design - works on desktop, tablet, and mobile")
    print("👥 Suitable for:")
    print("   • Business executives and managers")
    print("   • Technical teams and developers")
    print("   • Security and risk management teams")
    print("   • Compliance and audit personnel")
    print("   • Students and researchers")
    print("   • Project stakeholders and investors")
    print("\n⚡ Starting the enhanced dashboard server...")
    server.launch()