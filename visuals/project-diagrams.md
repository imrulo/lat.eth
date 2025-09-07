# Diagramas del Proyecto - Iniciativa Educativa LAT.ETH
## Diagramas Mermaid para Flujo de Eventos, Viaje del Participante, Asignación de Presupuesto y Hitos

**Tipo de Documento:** Documentación Visual del Proyecto  
**Proyecto:** Iniciativa Educativa LAT.ETH  
**Marco:** Modelo Educativo con Compromiso Cultural  

---

## 1. Diagrama de Flujo de Eventos

Este diagrama muestra la estructura del taller educativo de 3 horas:

```mermaid
graph TD
    A[Event Start] --> B[Hour 1: Cultural Engagement]
    B --> C[Dance Instruction]
    C --> D[Community Building]
    D --> E[Ice-breaking Activities]
    E --> F[Hour 2: Blockchain Education]
    F --> G[Blockchain Basics]
    G --> H[ENS Ecosystem Introduction]
    H --> I[LAT.ETH Domain Explanation]
    I --> J[Hour 3: Hands-on Learning]
    J --> K[Wallet Setup Assistance]
    K --> L[Subdomain Claiming]
    L --> M[POAP Recognition]
    M --> N[Event Completion]
    
    style A fill:#00ffff
    style B fill:#ff00ff
    style F fill:#ffff00
    style J fill:#00ff00
    style N fill:#00ffff
```

---

## 2. Diagrama del Viaje del Participante

Este diagrama muestra el viaje completo del participante desde la conciencia hasta el compromiso continuo:

```mermaid
journey
    title Participant Educational Journey
    section Awareness
      See Event Marketing: 5: Participant
      Register for Event: 4: Participant
    section Preparation
      Receive Pre-event Materials: 3: Participant
      Prepare for Workshop: 4: Participant
    section Event Experience
      Arrive at Venue: 5: Participant
      Participate in Dance Activities: 5: Participant
      Learn Blockchain Basics: 4: Participant
      Create Wallet: 3: Participant
      Claim LAT.ETH Subdomain: 5: Participant
      Receive POAP: 5: Participant
    section Post-Event
      Join Discord Community: 4: Participant
      Continue Learning: 4: Participant
      Use ENS Domain: 5: Participant
      Recommend to Friends: 5: Participant
```

---

## 3. Diagrama de Asignación de Presupuesto

Este diagrama muestra la distribución del presupuesto a través de los niveles del Marco Lógico:

```mermaid
pie title Budget Allocation by Logical Framework Level
    "GOAL Level (Educational Impact)" : 30
    "PURPOSE Level (Educational Model)" : 30
    "COMPONENTS Level (Educational Infrastructure)" : 40
```

---

## 4. Desglose Detallado del Presupuesto

Este diagrama muestra la asignación detallada del presupuesto a través de todas las categorías:

```mermaid
pie title Detailed Budget Breakdown (15,000 USDC)
    "Event Logistics" : 23.3
    "Specialized Personnel" : 23.3
    "Mobile Equipment & Transportation" : 15
    "Event Permits & Legal Requirements" : 8
    "Marketing & Outreach" : 8
    "Administrative & Project Management" : 8
    "ENS Technology & Gas Fees" : 7.3
    "Documentation & Media" : 6
    "Technical Infrastructure" : 4
    "Contingency & Emergency Fund" : 5.7
```

---

## 5. Hitos de Financiación Progresiva

Este diagrama muestra el sistema de desbloqueo de financiación progresiva:

```mermaid
gantt
    title Hitos de Financiación Progresiva
    dateFormat  YYYY-MM-DD
    section Mes 1
    Fundación y Configuración    :milestone, m1, 2024-01-01, 0d
    section Mes 2
    160 Latin Lovers Educados    :milestone, m2, 2024-02-01, 0d
    section Mes 3
    320 Latin Lovers Educados    :milestone, m3, 2024-03-01, 0d
    section Mes 4
    480 Latin Lovers Educados    :milestone, m4, 2024-04-01, 0d
    section Mes 5
    800 Latin Lovers Educados   :milestone, m5, 2024-05-01, 0d
```

---

## 6. Estrategia de Expansión Balcánica

Este diagrama muestra el cronograma de expansión a través de los países balcánicos:

```mermaid
gantt
    title Cronograma de Expansión Balcánica
    dateFormat  YYYY-MM-DD
    section Piloto Serbia
    Fundación y Configuración    :done, serbia1, 2024-01-01, 2024-01-31
    Implementación        :done, serbia2, 2024-02-01, 2024-04-30
    Evaluación            :done, serbia3, 2024-05-01, 2024-05-31
    section Croacia
    Evaluación y Configuración    :croatia1, 2024-06-01, 2024-07-31
    Implementación        :croatia2, 2024-08-01, 2024-10-31
    section Bosnia
    Evaluación y Configuración    :bosnia1, 2024-07-01, 2024-08-31
    Implementación        :bosnia2, 2024-09-01, 2024-11-30
    section Montenegro
    Evaluación y Configuración    :montenegro1, 2024-08-01, 2024-09-30
    Implementación        :montenegro2, 2024-10-01, 2024-12-31
    section Albania
    Evaluación y Configuración    :albania1, 2024-09-01, 2024-10-31
    Implementación        :albania2, 2024-11-01, 2025-01-31
    section Macedonia del Norte
    Evaluación y Configuración    :macedonia1, 2024-10-01, 2024-11-30
    Implementación        :macedonia2, 2024-12-01, 2025-02-28
    section Kosovo
    Evaluación y Configuración    :kosovo1, 2024-11-01, 2024-12-31
    Implementación        :kosovo2, 2025-01-01, 2025-03-31
```

---

## 7. Flujo de Impacto Educativo

Este diagrama muestra cómo las actividades educativas llevan a resultados medibles:

```mermaid
graph LR
    A[Educational Workshops] --> B[Blockchain Learning]
    B --> C[ENS Understanding]
    C --> D[Wallet Creation]
    D --> E[Subdomain Claiming]
    E --> F[POAP Recognition]
    F --> G[Community Engagement]
    G --> H[Continued Learning]
    H --> I[ENS Adoption]
    
    A --> J[800 Latin Lovers]
    B --> K[90% Understanding Rate]
    C --> L[80% ENS Knowledge]
    D --> M[85% Wallet Success]
    E --> N[800+ Subdomains]
    F --> O[800+ POAPs]
    G --> P[5 Active Communities]
    H --> Q[80% Retention]
    I --> R[800 New ENS Users]
    
    style A fill:#00ffff
    style I fill:#00ff00
    style R fill:#ff00ff
```

---

## 8. Risk Management Matrix

This diagram shows the risk assessment and mitigation strategies:

```mermaid
graph TD
    A[Project Risks] --> B[Technical Complexity]
    A --> C[Low Engagement]
    A --> D[Language Barriers]
    A --> E[Technology Resistance]
    
    B --> B1[Simplified Explanations]
    B --> B2[Step-by-step Guidance]
    
    C --> C1[Interactive Activities]
    C --> C2[Cultural Engagement Tools]
    
    D --> D1[Multilingual Materials]
    D --> D2[Local Language Support]
    
    E --> E1[Patient Instruction]
    E --> E2[Hands-on Support]
    
    style A fill:#ff0000
    style B1 fill:#00ff00
    style C1 fill:#00ff00
    style D1 fill:#00ff00
    style E1 fill:#00ff00
```

---

## 9. Team Structure and Responsibilities

This diagram shows the organizational structure and responsibilities:

```mermaid
graph TD
    A[Project Manager] --> B[Educational Project Manager]
    A --> C[Blockchain Specialists]
    A --> D[Dance Instructors]
    A --> E[Educational Coordinators]
    
    B --> B1[Overall Coordination]
    B --> B2[Progress Monitoring]
    B --> B3[Stakeholder Management]
    
    C --> C1[ENS Education]
    C --> C2[Technical Support]
    C --> C3[Blockchain Training]
    
    D --> D1[Cultural Engagement]
    D --> D2[Community Building]
    D --> D3[Event Facilitation]
    
    E --> E1[Community Engagement]
    E --> E2[Learning Support]
    E --> E3[Participant Assistance]
    
    style A fill:#00ffff
    style B fill:#ff00ff
    style C fill:#ffff00
    style D fill:#00ff00
    style E fill:#ff8000
```

---

## 10. Dashboard de Métricas de Éxito

Este diagrama muestra los indicadores clave de rendimiento y sus relaciones:

```mermaid
graph LR
    A[Educational Success] --> B[800 Latin Lovers]
    A --> C[90% Understanding Rate]
    A --> D[85% Wallet Success]
    A --> E[80% ENS Knowledge]
    
    F[Community Impact] --> G[5 Active Communities]
    F --> H[80% Retention Rate]
    F --> I[800+ Subdomains]
    F --> J[800+ POAPs]
    
    K[Technical Achievement] --> L[20 Events Completed]
    K --> M[100% Infrastructure]
    K --> N[Zero Technical Failures]
    K --> O[100% Venue Success]
    
    style A fill:#00ffff
    style F fill:#ff00ff
    style K fill:#ffff00
```

---

## 11. Visión a Largo Plazo y Escalamiento

Este diagrama muestra la progresión del piloto a escala internacional:

```mermaid
graph TD
    A[Serbia Pilot] --> B[Balkan Expansion]
    B --> C[International Scale]
    
    A --> A1[800 Latin Lovers]
    A --> A2[20 Events]
    A --> A3[5 Months]
    A --> A4[15,000 USDC]
    
    B --> B1[4,800 Latin Lovers]
    B --> B2[120 Events]
    B --> B3[12 Months]
    B --> B4[90,000 USDC]
    
    C --> C1[20,000+ Latin Lovers]
    C --> C2[500+ Events]
    C --> C3[24+ Months]
    C --> C4[375,000+ USDC]
    
    style A fill:#00ffff
    style B fill:#ff00ff
    style C fill:#ffff00
```

---

## 12. Alineación con ENS DAO

Este diagrama muestra cómo el proyecto se alinea con los objetivos del ENS DAO:

```mermaid
graph LR
    A[ENS DAO Objectives] --> B[User Onboarding]
    A --> C[Global Accessibility]
    A --> D[Educational Initiatives]
    A --> E[Ecosystem Growth]
    A --> F[Innovation]
    
    B --> B1[800 Latin Lovers]
    C --> C1[Expansión Región Balcánica]
    D --> D1[Educación Blockchain]
    E --> E1[Comunidades Web3]
    F --> F1[Modelo de Compromiso Cultural]
    
    style A fill:#00ffff
    style B1 fill:#00ff00
    style C1 fill:#00ff00
    style D1 fill:#00ff00
    style E1 fill:#00ff00
    style F1 fill:#00ff00
```

---

## Conclusión

Estos diagramas Mermaid proporcionan una representación visual integral de la Iniciativa Educativa LAT.ETH, mostrando:

1. **Flujo de Eventos**: Estructura clara de talleres de 3 horas
2. **Viaje del Participante**: Experiencia educativa completa
3. **Asignación de Presupuesto**: Distribución transparente de fondos
4. **Hitos Progresivos**: Sistema de financiación basado en hitos
5. **Estrategia de Expansión**: Escalamiento balcánico e internacional
6. **Impacto Educativo**: Resultados de aprendizaje medibles
7. **Gestión de Riesgos**: Estrategias de mitigación integrales
8. **Estructura del Equipo**: Responsabilidades organizacionales claras
9. **Métricas de Éxito**: Indicadores clave de rendimiento
10. **Visión a Largo Plazo**: Escalamiento del piloto a internacional
11. **Alineación ENS DAO**: Alineación clara de objetivos

Estas representaciones visuales hacen el proyecto más accesible y demuestran el enfoque profesional y estructurado para la educación blockchain a través del compromiso cultural.
