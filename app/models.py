"""
Modelos de datos para la aplicación de finanzas
"""
from datetime import datetime
from app.firebase_config import db

class SavingsAccount:
    """Modelo para cuentas de ahorro"""
    collection_name = 'savings_accounts'

    @staticmethod
    def get_all():
        """Obtiene todas las cuentas de ahorro"""
        if db is None:
            return []
        accounts = []
        docs = db.collection(SavingsAccount.collection_name).stream()
        for doc in docs:
            account = doc.to_dict()
            account['id'] = doc.id
            accounts.append(account)
        return accounts

    @staticmethod
    def get_by_id(account_id):
        """Obtiene una cuenta por ID"""
        if db is None:
            return None
        doc = db.collection(SavingsAccount.collection_name).document(account_id).get()
        if doc.exists:
            account = doc.to_dict()
            account['id'] = doc.id
            return account
        return None

    @staticmethod
    def create(data):
        """Crea una nueva cuenta de ahorro"""
        if db is None:
            return None
        data['created_at'] = datetime.now()
        data['updated_at'] = datetime.now()
        doc_ref = db.collection(SavingsAccount.collection_name).document()
        doc_ref.set(data)
        return doc_ref.id

    @staticmethod
    def update(account_id, data):
        """Actualiza una cuenta existente"""
        if db is None:
            return False
        data['updated_at'] = datetime.now()
        db.collection(SavingsAccount.collection_name).document(account_id).update(data)
        return True

    @staticmethod
    def delete(account_id):
        """Elimina una cuenta"""
        if db is None:
            return False
        db.collection(SavingsAccount.collection_name).document(account_id).delete()
        return True

    @staticmethod
    def get_total_balance():
        """Calcula el balance total de todas las cuentas"""
        accounts = SavingsAccount.get_all()
        return sum(account.get('balance', 0) for account in accounts)


class CreditCard:
    """Modelo para tarjetas de crédito"""
    collection_name = 'credit_cards'

    @staticmethod
    def get_all():
        """Obtiene todas las tarjetas de crédito"""
        if db is None:
            return []
        cards = []
        docs = db.collection(CreditCard.collection_name).stream()
        for doc in docs:
            card = doc.to_dict()
            card['id'] = doc.id
            cards.append(card)
        return cards

    @staticmethod
    def get_by_id(card_id):
        """Obtiene una tarjeta por ID"""
        if db is None:
            return None
        doc = db.collection(CreditCard.collection_name).document(card_id).get()
        if doc.exists:
            card = doc.to_dict()
            card['id'] = doc.id
            return card
        return None

    @staticmethod
    def create(data):
        """Crea una nueva tarjeta de crédito"""
        if db is None:
            return None
        data['created_at'] = datetime.now()
        data['updated_at'] = datetime.now()
        doc_ref = db.collection(CreditCard.collection_name).document()
        doc_ref.set(data)
        return doc_ref.id

    @staticmethod
    def update(card_id, data):
        """Actualiza una tarjeta existente"""
        if db is None:
            return False
        data['updated_at'] = datetime.now()
        db.collection(CreditCard.collection_name).document(card_id).update(data)
        return True

    @staticmethod
    def delete(card_id):
        """Elimina una tarjeta"""
        if db is None:
            return False
        db.collection(CreditCard.collection_name).document(card_id).delete()
        return True

    @staticmethod
    def get_total_debt():
        """Calcula la deuda total de todas las tarjetas"""
        cards = CreditCard.get_all()
        return sum(card.get('current_balance', 0) for card in cards)

    @staticmethod
    def get_total_limit():
        """Calcula el límite total de crédito"""
        cards = CreditCard.get_all()
        return sum(card.get('credit_limit', 0) for card in cards)


class CardInstallment:
    """Modelo para compras en cuotas de tarjetas de crédito"""
    collection_name = 'card_installments'

    @staticmethod
    def get_all_by_card(card_id):
        """Obtiene todas las compras en cuotas de una tarjeta"""
        if db is None:
            return []
        installments = []
        # Eliminar order_by para evitar requerir índice compuesto
        docs = db.collection(CardInstallment.collection_name)\
            .where('card_id', '==', card_id)\
            .stream()
        for doc in docs:
            inst = doc.to_dict()
            inst['id'] = doc.id
            # Calcular cuotas restantes y pago mensual
            total_months = inst.get('total_months', 1)
            paid_months = inst.get('paid_months', 0)
            inst['remaining_months'] = total_months - paid_months
            inst['monthly_payment'] = inst.get('total_amount', 0) / total_months if total_months > 0 else 0
            installments.append(inst)

        # Ordenar en Python por fecha de compra (más reciente primero)
        installments.sort(key=lambda x: x.get('purchase_date', datetime.min), reverse=True)
        return installments

    @staticmethod
    def get_by_id(installment_id):
        """Obtiene una compra en cuotas por ID"""
        if db is None:
            return None
        doc = db.collection(CardInstallment.collection_name).document(installment_id).get()
        if doc.exists:
            inst = doc.to_dict()
            inst['id'] = doc.id
            return inst
        return None

    @staticmethod
    def create(data):
        """Registra una nueva compra en cuotas"""
        if db is None:
            return None
        data['created_at'] = datetime.now()
        data['updated_at'] = datetime.now()
        if 'paid_months' not in data:
            data['paid_months'] = 0
        doc_ref = db.collection(CardInstallment.collection_name).document()
        doc_ref.set(data)
        return doc_ref.id

    @staticmethod
    def update(installment_id, data):
        """Actualiza una compra en cuotas"""
        if db is None:
            return False
        data['updated_at'] = datetime.now()
        db.collection(CardInstallment.collection_name).document(installment_id).update(data)
        return True

    @staticmethod
    def delete(installment_id):
        """Elimina una compra en cuotas"""
        if db is None:
            return False
        db.collection(CardInstallment.collection_name).document(installment_id).delete()
        return True

    @staticmethod
    def get_monthly_payment_for_card(card_id):
        """Calcula el pago mensual total de cuotas activas para una tarjeta"""
        installments = CardInstallment.get_all_by_card(card_id)
        total_monthly = 0
        for inst in installments:
            remaining = inst.get('remaining_months', 0)
            if remaining > 0:
                total_monthly += inst.get('monthly_payment', 0)
        return total_monthly


class Cash:
    """Modelo para efectivo"""
    collection_name = 'cash'

    @staticmethod
    def get_all():
        """Obtiene todos los registros de efectivo"""
        if db is None:
            return []
        cash_list = []
        docs = db.collection(Cash.collection_name).stream()
        for doc in docs:
            cash = doc.to_dict()
            cash['id'] = doc.id
            cash_list.append(cash)
        return cash_list

    @staticmethod
    def get_by_id(cash_id):
        """Obtiene un registro de efectivo por ID"""
        if db is None:
            return None
        doc = db.collection(Cash.collection_name).document(cash_id).get()
        if doc.exists:
            cash = doc.to_dict()
            cash['id'] = doc.id
            return cash
        return None

    @staticmethod
    def create(data):
        """Crea un nuevo registro de efectivo"""
        if db is None:
            return None
        data['created_at'] = datetime.now()
        data['updated_at'] = datetime.now()
        doc_ref = db.collection(Cash.collection_name).document()
        doc_ref.set(data)
        return doc_ref.id

    @staticmethod
    def update(cash_id, data):
        """Actualiza un registro de efectivo"""
        if db is None:
            return False
        data['updated_at'] = datetime.now()
        db.collection(Cash.collection_name).document(cash_id).update(data)
        return True

    @staticmethod
    def delete(cash_id):
        """Elimina un registro de efectivo"""
        if db is None:
            return False
        db.collection(Cash.collection_name).document(cash_id).delete()
        return True

    @staticmethod
    def get_total():
        """Calcula el total de efectivo"""
        cash_list = Cash.get_all()
        return sum(c.get('amount', 0) for c in cash_list)


class SavingsGoal:
    """Modelo para metas de ahorro"""
    collection_name = 'savings_goals'

    @staticmethod
    def get_all():
        """Obtiene todas las metas de ahorro"""
        if db is None:
            return []
        goals = []
        docs = db.collection(SavingsGoal.collection_name).stream()
        for doc in docs:
            goal = doc.to_dict()
            goal['id'] = doc.id
            # Calcular progreso
            current = goal.get('current_amount', 0)
            target = goal.get('target_amount', 1)
            goal['progress'] = (current / target * 100) if target > 0 else 0
            goals.append(goal)
        return goals

    @staticmethod
    def get_by_id(goal_id):
        """Obtiene una meta por ID"""
        if db is None:
            return None
        doc = db.collection(SavingsGoal.collection_name).document(goal_id).get()
        if doc.exists:
            goal = doc.to_dict()
            goal['id'] = doc.id
            current = goal.get('current_amount', 0)
            target = goal.get('target_amount', 1)
            goal['progress'] = (current / target * 100) if target > 0 else 0
            return goal
        return None

    @staticmethod
    def create(data):
        """Crea una nueva meta de ahorro"""
        if db is None:
            return None
        data['created_at'] = datetime.now()
        data['updated_at'] = datetime.now()
        if 'current_amount' not in data:
            data['current_amount'] = 0
        doc_ref = db.collection(SavingsGoal.collection_name).document()
        doc_ref.set(data)
        return doc_ref.id

    @staticmethod
    def update(goal_id, data):
        """Actualiza una meta existente"""
        if db is None:
            return False
        data['updated_at'] = datetime.now()
        db.collection(SavingsGoal.collection_name).document(goal_id).update(data)
        return True

    @staticmethod
    def delete(goal_id):
        """Elimina una meta"""
        if db is None:
            return False
        db.collection(SavingsGoal.collection_name).document(goal_id).delete()
        return True


class Loan:
    """Modelo para préstamos"""
    collection_name = 'loans'

    @staticmethod
    def get_all():
        """Obtiene todos los préstamos"""
        if db is None:
            return []
        loans = []
        docs = db.collection(Loan.collection_name).stream()
        for doc in docs:
            loan = doc.to_dict()
            loan['id'] = doc.id
            # Calcular progreso de pago
            total = loan.get('total_amount', 0)
            paid = loan.get('paid_amount', 0)
            remaining = total - paid
            loan['remaining_amount'] = remaining
            loan['progress'] = (paid / total * 100) if total > 0 else 0
            loans.append(loan)
        return loans

    @staticmethod
    def get_by_id(loan_id):
        """Obtiene un préstamo por ID"""
        if db is None:
            return None
        doc = db.collection(Loan.collection_name).document(loan_id).get()
        if doc.exists:
            loan = doc.to_dict()
            loan['id'] = doc.id
            total = loan.get('total_amount', 0)
            paid = loan.get('paid_amount', 0)
            remaining = total - paid
            loan['remaining_amount'] = remaining
            loan['progress'] = (paid / total * 100) if total > 0 else 0
            return loan
        return None

    @staticmethod
    def create(data):
        """Crea un nuevo préstamo"""
        if db is None:
            return None
        data['created_at'] = datetime.now()
        data['updated_at'] = datetime.now()
        if 'paid_amount' not in data:
            data['paid_amount'] = 0
        doc_ref = db.collection(Loan.collection_name).document()
        doc_ref.set(data)
        return doc_ref.id

    @staticmethod
    def update(loan_id, data):
        """Actualiza un préstamo existente"""
        if db is None:
            return False
        data['updated_at'] = datetime.now()
        db.collection(Loan.collection_name).document(loan_id).update(data)
        return True

    @staticmethod
    def delete(loan_id):
        """Elimina un préstamo"""
        if db is None:
            return False
        db.collection(Loan.collection_name).document(loan_id).delete()
        return True

    @staticmethod
    def get_total_debt():
        """Calcula la deuda total de todos los préstamos"""
        loans = Loan.get_all()
        return sum(loan.get('remaining_amount', 0) for loan in loans)

    @staticmethod
    def get_total_paid():
        """Calcula el total pagado de todos los préstamos"""
        loans = Loan.get_all()
        return sum(loan.get('paid_amount', 0) for loan in loans)


class FinancialSummary:
    """Clase para calcular resúmenes financieros"""

    @staticmethod
    def get_summary():
        """Obtiene un resumen completo de las finanzas"""
        total_savings = SavingsAccount.get_total_balance()
        total_cash = Cash.get_total()
        total_debt = CreditCard.get_total_debt()
        total_credit_limit = CreditCard.get_total_limit()

        total_assets = total_savings + total_cash
        net_worth = total_assets - total_debt

        # Porcentaje de uso de crédito
        credit_usage = (total_debt / total_credit_limit * 100) if total_credit_limit > 0 else 0

        return {
            'total_assets': total_assets,
            'total_savings': total_savings,
            'total_cash': total_cash,
            'total_debt': total_debt,
            'total_credit_limit': total_credit_limit,
            'available_credit': total_credit_limit - total_debt,
            'credit_usage_percent': credit_usage,
            'net_worth': net_worth
        }


class MonthlyBudget:
    """Clase para calcular y gestionar el balance mensual"""
    collection_name = 'monthly_budgets'

    @staticmethod
    def get_current_budget():
        """Obtiene o crea el presupuesto del mes actual"""
        if db is None:
            return None

        # Buscar presupuesto del mes actual
        current_month = datetime.now().strftime('%Y-%m')

        docs = db.collection(MonthlyBudget.collection_name)\
            .where('month', '==', current_month)\
            .limit(1)\
            .stream()

        for doc in docs:
            budget = doc.to_dict()
            budget['id'] = doc.id
            return budget

        # Si no existe, crear uno nuevo con valores por defecto
        default_budget = {
            'month': current_month,
            'salary': 0,
            'fixed_expenses': [],
            'include_loans': True,
            'include_credit_cards': True,
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        }

        doc_ref = db.collection(MonthlyBudget.collection_name).document()
        doc_ref.set(default_budget)
        default_budget['id'] = doc_ref.id

        return default_budget

    @staticmethod
    def update_budget(budget_id, data):
        """Actualiza el presupuesto mensual"""
        if db is None:
            return False
        data['updated_at'] = datetime.now()
        db.collection(MonthlyBudget.collection_name).document(budget_id).update(data)
        return True

    @staticmethod
    def calculate_monthly_balance():
        """Calcula el balance mensual completo"""
        budget = MonthlyBudget.get_current_budget()
        if not budget:
            return None

        # Ingresos
        salary = budget.get('salary', 0)

        # Gastos fijos personalizados
        fixed_expenses = budget.get('fixed_expenses', [])
        total_fixed_expenses = sum(exp.get('amount', 0) for exp in fixed_expenses)

        # Préstamos (si están activados)
        loans_payment = 0
        if budget.get('include_loans', True):
            loans = Loan.get_all()
            for loan in loans:
                if loan.get('remaining_amount', 0) > 0:
                    loans_payment += loan.get('monthly_payment', 0) or 0

        # Tarjetas de crédito (si están activadas)
        cards_payment = 0
        if budget.get('include_credit_cards', True):
            cards = CreditCard.get_all()
            for card in cards:
                # Obtener pago mensual de cuotas
                installments_payment = CardInstallment.get_monthly_payment_for_card(card['id'])

                # Calcular consumos de contado
                installments = CardInstallment.get_all_by_card(card['id'])
                total_pending = 0
                for inst in installments:
                    if inst.get('remaining_months', 0) > 0:
                        total_pending += inst['remaining_months'] * inst['monthly_payment']

                current_balance = card.get('current_balance', 0)
                regular_consumption = max(0, current_balance - total_pending)

                card_total = regular_consumption + installments_payment
                cards_payment += card_total

        # Calcular totales
        total_expenses = total_fixed_expenses + loans_payment + cards_payment
        balance = salary - total_expenses
        savings_capacity = max(0, balance)

        return {
            'salary': salary,
            'fixed_expenses': fixed_expenses,
            'total_fixed_expenses': total_fixed_expenses,
            'loans_payment': loans_payment,
            'cards_payment': cards_payment,
            'total_expenses': total_expenses,
            'balance': balance,
            'savings_capacity': savings_capacity,
            'budget_id': budget.get('id'),
            'include_loans': budget.get('include_loans', True),
            'include_credit_cards': budget.get('include_credit_cards', True)
        }


class PersonalLoan:
    """Clase para gestionar préstamos personales (yo pagué / me pagaron)"""
    collection_name = 'personal_loans'

    @staticmethod
    def get_all():
        """Obtiene todos los préstamos personales"""
        if db is None:
            return []
        loans = []
        docs = db.collection(PersonalLoan.collection_name).stream()
        for doc in docs:
            loan = doc.to_dict()
            loan['id'] = doc.id
            loans.append(loan)
        return loans

    @staticmethod
    def get_by_id(loan_id):
        """Obtiene un préstamo por ID"""
        if db is None:
            return None
        doc = db.collection(PersonalLoan.collection_name).document(loan_id).get()
        if doc.exists:
            loan = doc.to_dict()
            loan['id'] = doc.id
            return loan
        return None

    @staticmethod
    def create(data):
        """Crea un nuevo préstamo personal"""
        if db is None:
            return None
        data['created_at'] = datetime.now()
        data['updated_at'] = datetime.now()
        if 'status' not in data:
            data['status'] = 'pending'
        doc_ref = db.collection(PersonalLoan.collection_name).document()
        doc_ref.set(data)
        return doc_ref.id

    @staticmethod
    def update(loan_id, data):
        """Actualiza un préstamo personal"""
        if db is None:
            return False
        data['updated_at'] = datetime.now()
        db.collection(PersonalLoan.collection_name).document(loan_id).update(data)
        return True

    @staticmethod
    def delete(loan_id):
        """Elimina un préstamo personal"""
        if db is None:
            return False
        db.collection(PersonalLoan.collection_name).document(loan_id).delete()
        return True

    @staticmethod
    def get_summary():
        """Obtiene resumen de préstamos personales"""
        loans = PersonalLoan.get_all()

        total_lent = 0  # Yo pagué (me deben)
        total_borrowed = 0  # Me pagaron (yo debo)
        pending_lent = 0
        pending_borrowed = 0

        for loan in loans:
            amount = loan.get('amount', 0)
            loan_type = loan.get('type', 'lent')
            status = loan.get('status', 'pending')

            if loan_type == 'lent':
                total_lent += amount
                if status == 'pending':
                    pending_lent += amount
            else:
                total_borrowed += amount
                if status == 'pending':
                    pending_borrowed += amount

        return {
            'total_lent': total_lent,
            'total_borrowed': total_borrowed,
            'pending_lent': pending_lent,
            'pending_borrowed': pending_borrowed,
            'balance': pending_lent - pending_borrowed
        }

